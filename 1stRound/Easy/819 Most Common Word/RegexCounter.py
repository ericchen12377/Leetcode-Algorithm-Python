import collections
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        p = re.compile(r"[!?',;.]")
        sub_para = p.sub(' ', paragraph.lower())
        words = sub_para.split(' ')
        words = [word for word in words if word and word not in banned]
        count = collections.Counter(words)
        return count.most_common(1)[0][0]
