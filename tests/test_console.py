import unittest
from ..console import HBNBCommand

class TestCreateCommand(unittest.TestCase):
    """test the updated create command"""
    def test_missing_params(self):
        """test for availability of parameters"""
        cmd = HBNBCommand()
        cmd.do_create('')
        self.assertIn("** class name missing **", cmd._output)

    def test_createinstance(self):
        """test for an instance created with valid params"""
        cmd = HBNBCommand()
        cmd.do_create('TestClass')
        self.assertTrue(cmd._output.strip().isdigit())

    def test_missing_class(self):
        """tests for missing class"""
        cmd = HBNBCommand()
        cmd.do_create('non-existentclass')
        self.assertIn("** class doesn't exist **", cmd._output)

if __name__ == '__main__':
    unittest.main()
