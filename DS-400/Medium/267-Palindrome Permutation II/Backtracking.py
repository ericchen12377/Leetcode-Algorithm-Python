class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Get dictionary map char to its appearance
        counter = collections.Counter(s)
        mid, base, res = '', '', []
        # Get mid char and base string
        for c in counter:
            if counter[c] % 2 != 0:
                if mid:
                    return []
                else:
                    mid = c
            base += c * (counter[c] // 2)
        # Start backtracking
        self.backTracking(base, 0, mid, res)
        return res

    def backTracking(self, base, start, mid, res):
        # No char to be permuted, which means reach out the leaf in the tree
        if start == len(base):
            res.append(base + mid + base[::-1])
            return
        # Loop to permute char @ start with itself and all following different char
        for i in range(start, len(base)):
            # Prune the branch as duplicated!!!
            if i > start and (base[i] == base[i-1] or base[i] == base[start]):
                continue
            # Get the permutation
            perm = base if i == start else base[:start] + \
                base[i] + base[start+1:i] + base[start] + base[i+1:]
            # Permute next char with following chars
            self.backTracking(perm, start+1, mid, res)

# Take aabbbcc as an example

# counter would be {"a":2, "b":3, "c":2}

# After preprocess: baseStr = "abc", mid = "b" (if there is no char happens odd times, mid = "")

# Then use backtracking to find all the permutation of baseStr,

# the valid palindrome would be "permuStr + mid + reverseOfPermuStr"
