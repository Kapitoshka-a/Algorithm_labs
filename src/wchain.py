from typing import List, Tuple, Dict, Set


def initialise_groups(max_word_length: int) -> List[List]:
    """Initialise a list with all groups of words"""
    word_groups = []
    for i in range(max_word_length):
        word_groups.append([])

    return word_groups


def groups_of_words(file: str) -> Tuple[int, List[List[str]]]:
    """Move all word to each group of words sorting by their length"""
    with open(file, encoding='utf-8') as file:
        words = file.readlines()
        number_of_words = int(words[0])
        max_word_length = len(max(words, key=lambda w: len(w.strip())))
        word_groups = initialise_groups(max_word_length)

        for word in words[1:]:
            word = word.strip()
            word_group_index = len(word) - 1
            word_groups[word_group_index].append(word)

        return number_of_words, word_groups


def possible_words(word: str) -> Set:
    """Find all possible combinations of letters for next step"""
    derivative_words = []
    for index in range(len(word)):
        word_list = list(word)
        word_list.pop(index)
        derivative_words.append(''.join(word_list))

    return set(derivative_words)


def next_possible_words(word, next_word_group: List[str]) -> Set:
    """Find possible combinations of letters that are in next group"""
    derivative_words = possible_words(word)
    next_words = derivative_words.intersection(set(next_word_group))
    return next_words


def dfs(word: str, word_groups: List[List[str]], index: int, memorized_words: Dict[str, int]) -> int:
    """Find max chain for current word and memorize visited ones"""
    if word in memorized_words:
        return memorized_words[word]

    max_chain = 1
    next_words = next_possible_words(word, word_groups[index - 1])
    for next_word in next_words:
        index -= 1
        max_chain = max(max_chain, 1 + dfs(next_word, word_groups, index, memorized_words))

    memorized_words[word] = max_chain
    return max_chain


def max_word_chain(file: str) -> int:
    """Find max chain of words for given file"""
    number_of_words, word_groups = groups_of_words(file)
    memorized_words = dict()
    max_chain = 0

    for word_group_index in range(len(word_groups), 0, -1):
        for word in word_groups[word_group_index - 1]:
            max_chain = max(max_chain, dfs(word, word_groups, word_group_index - 1, memorized_words))

    return max_chain
