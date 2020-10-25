class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x: x[0])
        res = [newInterval]
        for interval in intervals:
            if newInterval[0] > interval[1]:
                if not res:
                    res.append(interval)
                else:
                    res[-1] = interval
                    res.append(newInterval)
            elif newInterval[1] < interval[0]:
                res.append(interval)
            elif newInterval[0] <= interval[0] and newInterval[1] >= interval[1]:
                continue
            elif newInterval[0] >= interval[0] and newInterval[0] <= interval[1] and newInterval[1] >= interval[1]:
                res[-1][0] = min(interval[0], newInterval[0])
                res[-1][1] = max(interval[1], newInterval[1])
            elif newInterval[1] == interval[0]:
                res[-1][1] = max(interval[1], newInterval[1])
            elif newInterval[0] >= interval[0] and newInterval[0] <= interval[1] and newInterval[1] < interval[1]:
                res[-1][0] = min(interval[0], newInterval[0])
                res[-1][1] = max(interval[1], newInterval[1])
            elif newInterval[0] < interval[0] and newInterval[1] >= interval[0] and newInterval[1] < interval[1]:
                res[-1][0] = min(interval[0], newInterval[0])
                res[-1][1] = max(interval[1], newInterval[1])
        return res
            