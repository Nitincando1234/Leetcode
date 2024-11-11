class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1
        for i in range(len(points)):
            count = collections.defaultdict(int)
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1[0] == p2[0]:  # if x of both the points is same slope will be infinity
                    slope = float("inf")
                else:
                    slope = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
                count[slope] += 1
                res = max(res, count[slope] + 1)
        return res