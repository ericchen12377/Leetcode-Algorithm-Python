from collections import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        word_map = Counter(words)
        results = []
        word_size = len(words[0])
        num_word = len(words)
        list_size = word_size*num_word
        for i in range(len(s) - list_size + 1):
            seen = dict(word_map)
            word_used = 0
            for j in range(i, i + list_size, word_size):
                sub_str = s[j: j + word_size]
                if sub_str in seen and seen[sub_str] > 0:
                    seen[sub_str] -= 1
                    word_used += 1
                else:
                    break
            if word_used == num_word:
                results.append(i)
        return results