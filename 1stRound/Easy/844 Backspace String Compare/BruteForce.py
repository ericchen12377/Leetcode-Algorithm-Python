class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        
        """
        
        def buildstring(string):
            array = []
            for i in range(len(string)):
                if string[i] != '#':
                    array.append(string[i])
                else:
                    if array:
                        array.pop()
            return ''.join(array)
        finalS = buildstring(S)
        finalT = buildstring(T)
        return finalS == finalT
        