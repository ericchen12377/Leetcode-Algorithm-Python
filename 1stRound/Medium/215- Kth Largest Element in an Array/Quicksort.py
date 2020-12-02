class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(array, i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        
        def partition(array, left, right):
            pivotelement = array[right]
            partitionidx = left
            for j in range(left, right):
                if array[j] < pivotelement:
                    swap(array, partitionidx,j)
                    partitionidx+=1
            swap(array, partitionidx, right)
            return partitionidx
        
        
        def quicksort(array, left, right):
            if left < right:
                partitionidx = partition(array, left, right)
                quicksort(array, left, partitionidx - 1)
                quicksort(array, partitionidx + 1, right)
        
        idxtoFind = len(nums) - k
        quicksort(nums, 0, len(nums) - 1)
        return nums[idxtoFind]
        