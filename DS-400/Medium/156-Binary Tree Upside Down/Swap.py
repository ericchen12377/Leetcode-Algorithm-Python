class Solution(object):
    def upsideDownBinaryTree(self, root):
        prev = prev_right = None
        while root:
            root.right, root.left, prev_right, prev, root = prev, prev_right, root.right, root, root.left
        return prev