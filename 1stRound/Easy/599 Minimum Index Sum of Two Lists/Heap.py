import heapq
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        interest = dict()
        for i, l in enumerate(list1):
            interest[l] = [i, 100000]
        for j, l in enumerate(list2):
            if l in interest:
                interest[l][1] = j
        heap = [(sum(v), l) for l, v in interest.items()]
        heapq.heapify(heap)
        res = []
        smallest = -1
        while heap:
            cursum, curl = heapq.heappop(heap)
            if smallest == -1:
                smallest = cursum
            if smallest == cursum:
                res.append(curl)
            else:
                break
        return res
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
p = Solution()
print(p.findRestaurant(list1,list2))