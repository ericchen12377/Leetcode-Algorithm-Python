import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        heapq.heapify(h)

        for i, point in enumerate(points):
            dist = point[0]**2 + point[1]**2
            heapq.heappush(h, (dist, i))

        ans = []
        for i in range(K):
            p = heapq.heappop(h)
            ans.append(points[p[1]])

        return ans
