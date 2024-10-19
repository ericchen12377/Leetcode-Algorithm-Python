class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res









# running too long
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            target = nums[i]
            rest = nums[0:i] + nums[i+1:]
            print('rest',rest)
            if not rest or len(rest)<2:
                return list(res)
            else:
                left, right = 0, len(rest) - 1
                rest.sort()
                print('rest',rest)
                while left != right:
                    if rest[left] + rest[right] == target:
                        res.add(tuple([target, left, right]))
                    elif rest[left] + rest[right] > target:
                        right -= 1
                    elif rest[left] + rest[right] < target:
                        left += 1
                return [list(i) for i in res]



        