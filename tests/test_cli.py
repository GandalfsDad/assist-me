import unittest
from click.testing import CliRunner
from AssistMe import cli

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_simple(self):
        result = self.runner.invoke(cli, ['simple'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('model:', result.output)

    def test_chat(self):
        result = self.runner.invoke(cli, ['chat'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('model:', result.output)

if __name__ == '__main__':
    unittest.main()