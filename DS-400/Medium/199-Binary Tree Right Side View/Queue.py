# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root == None:
            return []
        result = []
        queue = deque()
        queue.appendleft(root)
        while queue:
            levelSize = len(queue)
            result.append((queue[0]).val)
            for _ in range(levelSize):
                currentNode = queue.pop()
                if currentNode.left:
                    queue.appendleft(currentNode.left)
                if currentNode.right:
                    queue.appendleft(currentNode.right)
        return result