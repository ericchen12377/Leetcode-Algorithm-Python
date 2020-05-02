# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        info = [] # the first element is sum of the level,the second element is nodes in this level
        def dfs(node, depth=0):
            if not node:
                return
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            # print(info)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root)
        return [s / float(c) for s,c in info]
