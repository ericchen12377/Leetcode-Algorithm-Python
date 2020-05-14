class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        commons = [word for word in list1 if word in list2] #find common words
        answer = []
        smallest = 1000000
        for common in commons: #compare index
            index1 = list1.index(common)
            index2 = list2.index(common)
            index = index1 + index2
            if smallest > index:
                smallest = index
                answer = [common]
            elif smallest == index:
                answer.append(common)
        return answer
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
p = Solution()
print(p.findRestaurant(list1,list2))