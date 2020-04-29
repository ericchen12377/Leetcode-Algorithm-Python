import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        count = collections.Counter()
        for cpdomain in cpdomains:
            times, domain = cpdomain.split(" ")
            times = int(times)
            count[domain] += times
            for i, c in enumerate(domain): #update subdomains
                if c == '.':
                    count[domain[i + 1 : ]] += times
        return [str(times) + " " + domain for domain, times in count.items()]
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
p = Solution()
print(p.subdomainVisits(cpdomains))