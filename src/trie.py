from typing import List


class Node:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def search_word(self, word: str):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def search_prefix(self, prefix: str):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return True


def trie_list(words: List[str]):
    trie = Trie()
    sorted_words = sorted(words, key=lambda w: len(w))
    for word in sorted_words:
        trie.insert(word)
    return trie


if __name__ == '__main__':
    my_words = ['apple', 'appendix', 'alphabet', 'apo', 'api']
    trie_list(my_words)
