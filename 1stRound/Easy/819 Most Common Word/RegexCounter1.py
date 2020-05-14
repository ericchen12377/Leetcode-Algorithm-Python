import collections
import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\w+", paragraph.lower())
        count = collections.Counter(x for x in paragraph if x not in banned)
        return count.most_common(1)[0][0]
