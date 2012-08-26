__author__ = 'kovshi'

import mask
import unittest

class TestLeader(unittest.TestCase):
    def test_get_mask(self):
        self.assertEqual(mask.get_mask('spam', []), '****')
        self.assertEqual(mask.get_mask('spam', ['a', 'p']), '*pa*')
        self.assertEqual(mask.get_mask('spam', ['a']), '**a*')
        self.assertEqual(mask.get_mask('spam', ['m', 'a', 'p', 's']), 'spam')
        self.assertEqual(mask.get_mask('', []), '')


if __name__ == '__main__':
    unittest.main()
