class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = {word:ind for ind,word in enumerate(list1)}
        dic2 = {word:ind for ind,word in enumerate(list2)}
        answer = []
        smallest = 1000000
        for word in dic1:
            if word in dic2:
                _sum = dic1[word] + dic2[word]
                if smallest > _sum:
                    smallest = _sum
                    answer = [word]
                elif smallest == _sum:
                    answer.append(word)
        return answer
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
p = Solution()
print(p.findRestaurant(list1,list2))