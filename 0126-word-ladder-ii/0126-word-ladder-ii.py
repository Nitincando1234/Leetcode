from collections import deque, defaultdict

class Solution:
    def __init__(self):
        # Map to store the word->level relationship.
        self.mpp = {}
        # List to store the final answer.
        self.ans = []
        self.b = ""

    def dfs(self, word, seq):
        # Base condition:
        # If the word equals beginWord, we have found one of the sequences.
        # Reverse the sequence and add it to the answer.
        if word == self.b:
            self.ans.append(seq[::-1])
            return

        steps = self.mpp[word]

        # Replace each character of the word with letters from 'a' to 'z'.
        # Check if the transformed word exists in the map and is one level below.
        for i in range(len(word)):
            original = word[i]
            for ch in range(ord('a'), ord('z') + 1):
                new_char = chr(ch)
                word = word[:i] + new_char + word[i + 1:]

                if word in self.mpp and self.mpp[word] + 1 == steps:
                    self.dfs(word, seq + [word])

            word = word[:i] + original + word[i + 1:]

    def findLadders(self, beginWord, endWord, wordList):
        # Add all words from wordList to a set for efficient lookups.
        word_set = set(wordList)

        # Perform BFS to find the shortest transformation sequences.
        queue = deque([beginWord])
        self.mpp[beginWord] = 1

        word_set.discard(beginWord)

        while queue:
            word = queue.popleft()
            steps = self.mpp[word]

            if word == endWord:
                break

            # Replace each character of the word with letters from 'a' to 'z'.
            for i in range(len(word)):
                original = word[i]
                for ch in range(ord('a'), ord('z') + 1):
                    new_char = chr(ch)
                    transformed = word[:i] + new_char + word[i + 1:]

                    if transformed in word_set:
                        queue.append(transformed)
                        word_set.discard(transformed)
                        self.mpp[transformed] = steps + 1

        # If the endWord is reached, perform DFS to find all paths.
        if endWord in self.mpp:
            self.b = beginWord
            self.dfs(endWord, [endWord])

        return self.ans




