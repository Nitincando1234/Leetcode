class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        currFile = ""
        for c in path + "/":
            if c == "/":
                if currFile == "..":
                    if stack: stack.pop()
                elif currFile != "." and currFile != "":
                    stack.append(currFile)
                currFile = ""
            else:
                currFile += c
        
        return "/" + "/".join(stack)