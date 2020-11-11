class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        visited = [True]*(len(s))
        queue = [0]
        
        while queue:
            start = queue.pop()
            if visited[start]:
                for i in range(start+1, len(s)+1):
                    if s[start:(i)] in wordset:
                        queue.append(i)
                        if i == len(s):
                            return True
                visited[start] = True
        return False