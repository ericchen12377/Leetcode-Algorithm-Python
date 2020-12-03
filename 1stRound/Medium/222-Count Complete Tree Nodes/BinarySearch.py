# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def getTreeHeight(root):
            height = 0
            while root.left:
                height+=1
                root = root.left
            return height
        
        def nodeExists(idxtoFind, height, node):
            left = 0
            right = 2 ** height - 1
            count = 0
            
            while count < height:
                midofNode = math.ceil((left + right) / 2)
                # print(midofNode)
                if idxtoFind >= midofNode:
                    node = node.right
                    left = midofNode
                    # print(left)
                else:
                    node = node.left
                    right = midofNode - 1
                count += 1
            return node != None
            
        
        height = getTreeHeight(root)
        if height == 0:
            return 1
        upperCount = 2 ** (height) - 1
        
        left, right = 0, upperCount
        
        while left < right:
            idxtoFind = math.ceil((left + right) / 2)
            if nodeExists(idxtoFind, height, root):
                left = idxtoFind 
            else:
                right = idxtoFind - 1
        # print(upperCount)
        # print(left)
        return upperCount + left + 1