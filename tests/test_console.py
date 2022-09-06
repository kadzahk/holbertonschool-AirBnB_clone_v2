#!/usr/bin/python3
"""Unittest for the console."""
import unittest
import console
import os
from io import StringIO
from unittest.mock import patch


HBNBCommand = console.HBNBCommand

class TestConsole(unittest.TestCase):
    """To test the console."""

    @classmethod
    def setUpClass(cls):
        """set up for the test."""
        cls.newconsole = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Launched at the end."""
        del cls.newconsole

    def tearDown(self):
        """Remove file.json"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    @unittest.skipIf(os.getenv("HBNBCommand") == "db", "Not using db")
    def test_create(self):
        """To test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.newconsole.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.newconsole.onecmd("create hello")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.newconsole.onecmd("create User")
            self.assertEqual("[[User]", f.getvalue()[:7])