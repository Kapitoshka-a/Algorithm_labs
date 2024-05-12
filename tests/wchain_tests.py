import os
import unittest
from src.wchain import groups_of_words, possible_words, next_possible_words, dfs, max_word_chain


class TestWChain(unittest.TestCase):
    def setUp(self):
        self.test_words_file = "test_roads.csv"
        with open(self.test_words_file, 'w') as file:
            lines = [
                "13\n",
                "ooooooooo\n",
                "crocodile\n",
                "rocodile\n",
                "crocodil\n",
                "croodile\n",
                "crocodi\n",
                "rocodil\n",
                "croco\n",
                "ooooo\n",
                "oooo\n",
                "ooo\n",
                "oo\n",
                "o\n"
            ]

            for line in lines:
                file.write(line)

    def tearDown(self):
        if os.path.exists(self.test_words_file):
            os.remove(self.test_words_file)

    def test_groups_of_words(self):
        number_of_words, word_groups = groups_of_words(self.test_words_file)
        self.assertEqual(number_of_words, 13)
        self.assertEqual(len(word_groups), 10)

    def test_possible_words(self):
        self.assertEqual(possible_words("word"), {"ord", "wrd", "wor", "wod"})

    def test_next_possible_words(self):
        self.assertEqual(next_possible_words("word", ["wor", "war", "wrd"]), {"wrd", "wor"})

    def test_dfs(self):
        word_groups = [["o"], ["wo"], ["wrd", "wor"]]
        memorized_words = {}
        self.assertEqual(dfs("word", word_groups, 3, memorized_words), 4)

    def test_max_word_chain(self):
        max_chain_length = max_word_chain(self.test_words_file)
        self.assertEqual(max_chain_length, 5)


if __name__ == '__main__':
    unittest.main()
