# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None: # if root is None, there is no deeper level to go to. Then, return [] which is the root. 
            return root
        
        res = [] # final output
        queue = [] # keep track of nodes in each level from left to right
        queue.append(root) # first node (root) is added to queue which we'll be later added to level and then finally res

        while len(queue) > 0: # we keep going until there is something in queue. Empty queue means we have covered every node
            level = [] # This collects every node is each level. Note the output format in the problem statement. Nodes of each level are a sublist within the final output list res
            for i in range(len(queue)): # it goes over length of queue which includes all the elements of current level, and each of them is added to the level variable. 
                node = queue.pop(0) # removes the first element of the list. In contrast to pop() that removes last element and is used for stack data structure. Note that first element is added 
                level.append(node.val) # append the value of current node
            
                if node.left != None: # queue gets updated by adding left child. The traversal occurs from left to right
                    queue.append(node.left)
                if node.right != None: # queue gets updated by adding right child. 
                    queue.append(node.right)
            res.append(level) # we're done with this level, and we append level to the res variable
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        queue = [root,]
        
        if not root:
            return levels
        
        while queue:
            level = []
            
            for i in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels

            