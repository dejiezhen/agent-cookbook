import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / 'skills'
        skill = self.source / 'example'
        (skill / 'references').mkdir(parents=True)
        (skill / 'SKILL.md').write_text('example skill')
        (skill / 'references' / 'guide.md').write_text('reference content')
        self.dest = self.root / 'project' / '.agents' / 'skills'
        self.tool = load_script('install_skills')

    def test_preview_does_not_create_destination(self):
        plan = self.tool.install(self.source, self.dest, ['example'])
        self.assertEqual(len(plan), 1)
        self.assertFalse(self.dest.exists())

    def test_apply_copies_complete_skill(self):
        self.tool.install(self.source, self.dest, ['example'], apply=True)
        self.assertEqual((self.dest / 'example/references/guide.md').read_text(), 'reference content')

    def test_collision_preserves_all_existing_content(self):
        (self.source / 'second').mkdir()
        (self.source / 'second/SKILL.md').write_text('second skill')
        (self.dest / 'second').mkdir(parents=True)
        marker = self.dest / 'second/SKILL.md'
        marker.write_text('user content')
        with self.assertRaises(FileExistsError):
            self.tool.install(self.source, self.dest, ['example', 'second'], apply=True)
        self.assertEqual(marker.read_text(), 'user content')
        self.assertFalse((self.dest / 'example').exists())

    def test_unknown_skill_creates_nothing(self):
        with self.assertRaises(ValueError):
            self.tool.install(self.source, self.dest, ['example', 'missing'], apply=True)
        self.assertFalse(self.dest.exists())

    def test_traversal_is_rejected(self):
        with self.assertRaises(ValueError):
            self.tool.install(self.source, self.dest, ['../escape'], apply=True)
        self.assertFalse(self.dest.exists())

    def test_overlapping_destination_is_rejected(self):
        with self.assertRaises(ValueError):
            self.tool.install(self.source, self.source / 'nested', ['example'], apply=True)

    def test_symlinked_source_is_rejected(self):
        (self.source / 'alias').symlink_to(self.source / 'example', target_is_directory=True)
        with self.assertRaises(ValueError):
            self.tool.install(self.source, self.dest, ['alias'], apply=True)

    def test_duplicate_names_are_rejected(self):
        with self.assertRaises(ValueError):
            self.tool.install(self.source, self.dest, ['example', 'example'], apply=True)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.skill = Path(self.tmp.name) / 'example'
        (self.skill / 'agents').mkdir(parents=True)
        self.manifest = self.skill / 'SKILL.md'
        self.manifest.write_text('---\nname: example\ndescription: Handle the example workflow.\n---\n# Example\nDo the task.\n')
        (self.skill / 'agents/openai.yaml').write_text('interface:\n  display_name: "Example"\n  short_description: "Handle a focused example workflow"\n  default_prompt: "Use $example to complete this task."\n')
        self.tool = load_script('validate_skills')

    def test_valid_skill(self):
        self.assertEqual(self.tool.validate_skill(self.skill), [])

    def test_name_must_match_folder(self):
        self.manifest.write_text(self.manifest.read_text().replace('name: example', 'name: other'))
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_empty_description_rejected(self):
        self.manifest.write_text('---\nname: example\ndescription: ""\n---\n# Example\n')
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_broken_reference_rejected(self):
        with self.manifest.open('a') as f:
            f.write('[Guide](references/missing.md)\n')
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_invalid_yaml_rejected(self):
        self.manifest.write_text('---\nname: [\n---\n# Example\n')
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_nonmapping_ui_interface_rejected(self):
        (self.skill / 'agents/openai.yaml').write_text('interface: []\n')
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_nested_broken_reference_rejected(self):
        (self.skill / 'references').mkdir()
        (self.skill / 'references/guide.md').write_text('[Missing](absent.md)')
        self.assertTrue(self.tool.validate_skill(self.skill))

    def test_all_repository_skills_validate(self):
        skills = list((ROOT / 'skills').iterdir())
        self.assertTrue(skills)
        for skill in skills:
            with self.subTest(skill=skill.name):
                self.assertEqual(self.tool.validate_skill(skill), [])


if __name__ == '__main__':
    unittest.main()
