class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = []
        res_set = {}
        size = -1
        for i in range(len(strs)):
            if str(sorted(list(strs[i]))) not in res_set:
                size += 1
                res_set[str(sorted(list(strs[i])))] = size
                res.append([])
                res[size].append(strs[i])
            else:
                res[res_set[str(sorted(list(strs[i])))]].append(strs[i])
        return res  

