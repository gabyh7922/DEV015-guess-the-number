import unittest
from utils import comparation_result


class TestComparationResultFunction(unittest.TestCase):

    def test_ok(self):
        self.assertEqual(comparation_result(3, 3), 'winner')
        self.assertEqual(comparation_result(3, 4), 'menor')
        self.assertEqual(comparation_result(4, 3), 'mayor')
    
    def test_errors(self):
        self.assertEqual(comparation_result("3", 3), 'error')
        self.assertEqual(comparation_result(3, "3"), 'error')
        self.assertEqual(comparation_result("l", 3), 'error')
        self.assertEqual(comparation_result(3, "l"), 'error')
        self.assertEqual(comparation_result(" ", "l"), 'error')
    
    def test_missing_arguments(self):
        with self.assertRaises(TypeError) as result:
            self.assertEqual(comparation_result(3,), 'error')
        self.assertEqual(
            str(result.exception), "comparation_result() missing 1 required positional argument: 'num'"
        )

        with self.assertRaises(TypeError) as result:
            self.assertEqual(comparation_result(), 'error')
        self.assertEqual(
            str(result.exception), "comparation_result() missing 2 required positional arguments: 'consult' and 'num'"
        )

    """def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)"""

if __name__ == '__main__':
    unittest.main()