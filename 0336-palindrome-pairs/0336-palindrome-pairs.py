class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {word: i for i, word in enumerate(words)}
        output = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[: j]
                right = word[j: ]
                reversed_left = left[:: -1]
                reversed_right = right[:: -1]
                if reversed_left in lookup and lookup[reversed_left] != i and reversed_right == right: output.append([i, lookup[reversed_left]])
                if j > 0 and reversed_right in lookup and lookup[reversed_right] != i and reversed_left == left: output.append([lookup[reversed_right], i])
        return output