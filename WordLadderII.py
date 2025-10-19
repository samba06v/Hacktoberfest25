from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        BFS + Backtracking approach to find all shortest transformation sequences.
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in wordSet:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
            wordSet -= set(new_layer.keys())
            layer = new_layer
        return []
