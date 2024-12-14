class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxDepth = 0
        depth_map = {0: 0}
        lines = input.split("\n")
        for line in lines:
            path = line.split("\t")[-1]
            depth = line.count("\t")
            # print(depth)
            if "." in path:
                maxDepth = max(len(path) + depth_map[depth], maxDepth)
            else:
                depth_map[depth + 1] = depth_map[depth] + len(path) + 1
        return maxDepth
                