class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            # print(s)
            if ''.join(sorted(s)) not in list(mp.keys()):
                mp[''.join(sorted(s))] = [s]
                print(mp)
            else:
                mp[''.join(sorted(s))].append(s)
        
        return [i for i in mp.values()]