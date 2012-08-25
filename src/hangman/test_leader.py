__author__ = 'kovshi'

from leader import HangmanLeader
import unittest

class TestLeader(unittest.TestCase):
    def test_get_mask(self):
        leader = HangmanLeader(None, None)
        self.assertEqual(leader.get_mask('spam', []), '****')
        self.assertEqual(leader.get_mask('spam', ['a']), '**a*')
        self.assertEqual(leader.get_mask('spam', ['a', 'p']), '*pa*')
        self.assertEqual(leader.get_mask('', []), '')
        self.assertEqual(leader.get_mask('spam', ['m', 'a', 'p', 's']), 'spam')


if __name__ == '__main__':
    unittest.main()
