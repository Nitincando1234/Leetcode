class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0
        
        while i < len(words):
            # Line Completes
            if length + len(line) + len(words[i]) > maxWidth:
                extra_spaces = maxWidth - length
                spaces = extra_spaces // max(1, len(line) - 1)
                remainder = extra_spaces % max(1, len(line) - 1)
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces
                    if remainder > 0:
                        line[j] += " "
                        remainder -= 1        
                res.append("".join(line))
                line, length = [], 0
            
            line.append(words[i])
            length += len(words[i])
            i += 1
        
        # Handling the last line
        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        res.append(last_line + trail_space * " ")
        return res