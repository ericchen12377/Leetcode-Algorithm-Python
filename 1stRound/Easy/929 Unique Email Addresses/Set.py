class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        eset = set()
        for email in emails:
            simper = self.simpifyEmail(email)
            eset.add(simper)
        return len(eset)
    
    def simpifyEmail(self, email):
        local, domain = email.split("@") 
        local = local.replace('.', '') 
        plus_i = local.find('+') # find index of +
        if plus_i != -1: # if + exists
            local = local[:plus_i] # substring before +
        return local + "@" + domain


emails = ["test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]
p = Solution()
print(p.numUniqueEmails(emails))