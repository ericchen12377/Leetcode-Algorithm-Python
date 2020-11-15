class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        p1,p2=0,0
        v1=version1.split('.')
        v2= version2.split('.')
        
        while p1<len(v1) and p2<len(v2):
            
            if int(v1[p1])>int(v2[p2]):
                return 1
            if int(v1[p1])<int(v2[p2]):
                return -1
            p1+=1
            p2+=1
            
        if len(v1)==len(v2): #if exit because both finished
            return 0
        if p1==len(v1): #exit because p1 is done check last compare it new p2
            while p2<len(v2):
                if int(v2[p2])>0:
                    return -1
                p2+=1
            return 0
        if p2==len(v2): #exit because p1 is done check last compare it new p2
            while p1<len(v1):
                if int(v1[p1])>0:
                    return 1
                p1+=1
            return 0