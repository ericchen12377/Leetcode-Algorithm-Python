class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s >= len_t:
            hash_s = dict()
            for i in range(len(s)):
                if s[i] in hash_s.keys():
                    hash_s[s[i]]+=1
                else:
                    hash_s[s[i]]=1
            # print(hash_s)
            for i in range(len(t)):
                if t[i] in hash_s.keys():
                    hash_s[t[i]]-=1
                else:
                    continue
            # print(hash_s)
            # print(all(list(hash_s.values())))
        else:
            hash_s = dict()
            for i in range(len(t)):
                if t[i] in hash_s.keys():
                    hash_s[t[i]]+=1
                else:
                    hash_s[t[i]]=1
            # print(hash_s)
            for i in range(len(s)):
                if s[i] in hash_s.keys():
                    hash_s[s[i]]-=1
                else:
                    continue
            # print(hash_s)
            # print(all(list(hash_s.values())))
        if all([v==0 for v in list(hash_s.values())]):
            return True
        else:
            return False
