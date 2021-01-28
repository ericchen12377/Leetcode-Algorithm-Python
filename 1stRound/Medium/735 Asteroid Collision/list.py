class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            res.append(a)
            i = len(res)-1
            while i > 0:
                if res[-2] < 0:
                    break
                elif res[-2] > 0 and res[-1] > 0:
                    break
                elif res[-2] > 0 and res[-1] < 0:
                    if abs(res[-2]) == abs(res[-1]):
                        res.pop()
                        res.pop()
                        break
                    elif abs(res[-2]) > abs(res[-1]):
                        res.pop()
                        break
                    elif abs(res[-2]) < abs(res[-1]):
                        res[-2], res[-1] = res[-1], res[-2]
                        res.pop()
                        i -= 1
        return res
