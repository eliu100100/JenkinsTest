import unittest
from helloworld import hello_world

class TestMethod(unittest.TestCase):
    def test_value(self):
        self.assertEqual(hello_world(), "hello world")

    def test_value_not_equal(self):
        self.assertNotEqual(hello_world(), "Hello World")

if __name__  == '__main__':
    unittest.main()