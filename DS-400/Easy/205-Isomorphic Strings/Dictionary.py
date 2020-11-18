class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word_dic = {}

        if(len(s)!=len(t)):
            return False
        else:
            for i in range(len(s)):
                if(s[i] in word_dic):
                    if(word_dic[s[i]]!=t[i]):
                        return False
                else:
                    if(t[i] in list(word_dic.values())):
                        return False
                    word_dic[s[i]] = t[i]

        return True