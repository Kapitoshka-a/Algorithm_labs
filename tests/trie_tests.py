import unittest
from src.trie import trie_list


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = trie_list(['apple', 'appendix', 'alphabet', 'apo', 'api'])

    def test_search_word(self):
        self.assertTrue(self.trie.search_word('apple'))
        self.assertTrue(self.trie.search_word('appendix'))
        self.assertTrue(self.trie.search_word('alphabet'))
        self.assertTrue(self.trie.search_word('apo'))
        self.assertTrue(self.trie.search_word('api'))

        self.assertFalse(self.trie.search_word('app'))
        self.assertFalse(self.trie.search_word('ap'))
        self.assertFalse(self.trie.search_word('xyz'))

    def test_search_prefix(self):
        self.assertTrue(self.trie.search_prefix('app'))
        self.assertTrue(self.trie.search_prefix('al'))
        self.assertTrue(self.trie.search_prefix('api'))

        self.assertFalse(self.trie.search_prefix('x'))


if __name__ == '__main__':
    unittest.main()
