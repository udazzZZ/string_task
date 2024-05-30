#!/usr/bin/env python3

"""
Suffix tree to search in dictionary
"""

from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.indexes = set()

class SuffixTree:
    def __init__(self):
        self.root = Node() 

    def build_tree(self, word: str, index: int) -> None:
        for i in range(len(word)):
            current = self.root
            for char in word[i:]:
                if char not in current.children:
                    current.children[char] = Node()
                current = current.children[char]
                current.indexes.add(index)
    
    def search(self, substring: str) -> List[int]:
        current = self.root
        for char in substring:
            if char not in current.children:
                return []
            current = current.children[char]
        return current.indexes

class SSet:
    """String set. Should be based on Suffix tree"""

    def __init__(self, fname: str) -> None:
        """Saves filename of a dictionary file"""
        self.fname = fname
        self.words = []
        self.tree = SuffixTree()

    def load(self) -> None:
        """
        Loads words from a dictionary file.
        Each line contains a word.
        File is not sorted.
        """
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]
            for i in range(len(self.words)):
                self.tree.build_tree(self.words[i], i)

    def search(self, substring: str) -> List[str]:
        idxs = self.tree.search(substring)
        return [self.words[i] for i in idxs]