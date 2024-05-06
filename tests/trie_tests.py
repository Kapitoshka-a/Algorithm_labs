import unittest
from src.trie import trie_list


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = trie_list(['apple', 'appendix', 'alphabet', 'apo', 'api'])
        self.trie_2 = trie_list(['apple', 'banana', 'cocos', 'orange'])

    def test_case_1(self):
        self.assertTrue(self.trie.search_word('apple'))
        self.assertTrue(self.trie.search_word('appendix'))
        self.assertTrue(self.trie.search_word('alphabet'))
        self.assertTrue(self.trie.search_word('apo'))
        self.assertTrue(self.trie.search_word('api'))

        self.assertFalse(self.trie.search_word('app'))
        self.assertFalse(self.trie.search_word('ap'))
        self.assertFalse(self.trie.search_word('xyz'))

    def test_case_2(self):
        self.assertTrue(self.trie.search_prefix('app'))
        self.assertTrue(self.trie.search_prefix('al'))
        self.assertTrue(self.trie.search_prefix('api'))

        self.assertFalse(self.trie.search_prefix('x'))

    def test_case_3(self):
        self.assertTrue(self.trie_2.search_word('apple'))
        self.assertTrue(self.trie_2.search_word('banana'))
        self.assertTrue(self.trie_2.search_word('orange'))
        self.assertTrue(self.trie_2.search_word('cocos'))

        self.assertFalse(self.trie.search_word('app'))
        self.assertFalse(self.trie.search_word('ap'))
        self.assertFalse(self.trie.search_word('xyz'))

    def test_case_4(self):
        self.assertTrue(self.trie_2.search_prefix('app'))
        self.assertTrue(self.trie_2.search_prefix('ba'))
        self.assertFalse(self.trie_2.search_prefix('lol'))


if __name__ == '__main__':
    unittest.main()
