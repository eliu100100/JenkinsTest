import unittest
from helloworld import hello_world

class TestMethod(unittest.TestCase):
    def test_value(self):
        self.assertEqual(hello_world(), "hello world")

if __name__  == '__main__':
    unittest.main()