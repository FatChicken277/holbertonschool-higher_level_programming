#!/usr/bin/python3
"""This module contains a class that test
    all functionality of the Base model.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Base class tests.
    """
    def setUp(self):
        """sets nb_objects to 0.
        """
        Base._Base__nb_objects = 0

    def test_docstring(self):
        """Test doc strings.
        """
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)

    def test_void_none(self):
        """Test with none value.
        """
        base = Base(None)
        self.assertEqual(base.id, 1)
        base = Base()
        self.assertEqual(base.id, 2)
        base = Base(3)
        self.assertEqual(base.id, 3)
        base = Base()
        self.assertEqual(base.id, 3)

    def test_int(self):
        """Test id attribute (int).
        """
        base = Base(-4)
        self.assertEqual(base.id, -4)
        base = Base()
        self.assertEqual(base.id, 1)

    def test_float(self):
        """Test id attribute (float).
        """
        base = Base(1.34)
        self.assertEqual(base.id, 1.34)

    def test_boolean(self):
        """Test id attribute (boolean).
        """
        base = Base(False)
        self.assertEqual(base.id, False)

    def test_string(self):
        """Test id attribute (str).
        """
        base = Base("a")
        self.assertEqual(base.id, "a")

    def test_tuple(self):
        """Test id attribute (tuple).
        """
        base = Base(())
        self.assertEqual(base.id, ())

    def test_list(self):
        """Test id attribute (list).
        """
        base = Base([])
        self.assertEqual(base.id, [])

    def test_dict(self):
        """Test id attribute (dict).
        """
        base = Base({})
        self.assertEqual(base.id, {})

    def test_set(self):
        """Test id attribute (set).
        """
        base = Base({1})
        self.assertEqual(base.id, {1})


if __name__ == "__main__":
    unittest.main()
