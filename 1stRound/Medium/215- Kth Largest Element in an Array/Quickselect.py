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
        
        
        def quickselect(array, left, right, idxtoFind):
            if left < right:
                partitionidx = partition(array, left, right)
                if partitionidx == idxtoFind:
                    return array[partitionidx]
                elif idxtoFind < partitionidx:
                    return quickselect(array, left, partitionidx - 1, idxtoFind)
                else:
                    return quickselect(array, partitionidx + 1, right, idxtoFind)
        
        idxtoFind = len(nums) - k
        quickselect(nums, 0, len(nums) - 1, idxtoFind)
        return nums[idxtoFind]