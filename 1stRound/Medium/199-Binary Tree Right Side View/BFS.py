# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels = []
        queue = [root,]
        
        if not root:
            return 
        
        while queue:
            level = []
            
            for i in range(len(queue)):
                node = queue[0]
                queue = queue[1:]
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level[-1])
        return levels


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels = []
        queue = [root,]
        
        if not root:
            return 
        
        while queue:
            # level = []
            
            for i in range(len(queue)):
                node = queue[0]
                queue = queue[1:]
                # level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(node.val)
        return levels