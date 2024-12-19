class Solution:
    def originalDigits(self, s: str) -> str:
        char_count = dict()
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        word_list = [
            ('zero', 'z', 0),
            ('two', 'w', 2),
            ('four', 'u', 4),
            ('six', 'x', 6),
            ('eight', 'g', 8),
            ('one', 'o', 1),
            ('three', 'r', 3),
            ('five', 'f', 5),
            ('seven', 'v', 7),
            ('nine', 'i', 9)
        ]
        
        # Reordering the list for proper processing
        word_list = [
            ('zero', 'z', 0),
            ('two', 'w', 2),
            ('four', 'u', 4),
            ('six', 'x', 6),
            ('eight', 'g', 8),
            ('one', 'o', 1),
            ('three', 'r', 3),
            ('five', 'f', 5),
            ('seven', 'v', 7),
            ('nine', 'i', 9)
        ]

        number_count = [0] * 10
        for word, unique_char, digit in word_list:
            unique_char_count = char_count.get(unique_char, 0)
            if unique_char_count > 0:
                number_count[digit] = unique_char_count
                for char in word:
                    char_count[char] = char_count.get(char, 0) - unique_char_count

        return "".join(str(number) * count for number, count in enumerate(number_count))
