class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False
                else:
                    changes[10] += 1
                    changes[5] -= 1
            elif bill == 20:
                if changes[10] != 0:
                    if changes[5] == 0:
                        return False
                    else:
                        changes[5] -= 1
                        changes[10] -= 1
                else:
                    if changes[5] < 3:
                        return False
                    else:
                        changes[5] -= 3
        return True
