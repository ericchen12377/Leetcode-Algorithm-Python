class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper() #upper case
        groups = ''.join(S.split('-')) #join
        bias = len(groups) % K #check how many for the left
        devides = len(groups) / K
        answer = groups[:bias]
        answer += '-' if bias != 0 else ''
        for i in range(devides):
            answer += groups[i*K+bias : (i+1)*K+bias] + '-' #reconstruct
        return answer[:-1]
