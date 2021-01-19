class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[1])
        visited = set()
        for s, e in events:
            for t in range(s, e+1):
                if t not in visited:
                    visited.add(t)
                    break
        return len(visited)