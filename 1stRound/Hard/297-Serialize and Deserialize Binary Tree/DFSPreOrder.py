# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def DFSPreorder(root):
            return [root.val] + DFSPreorder(root.left) + DFSPreorder(root.right)  if root else [None]
        print(' '.join(map(str, DFSPreorder(root))))
        return ' '.join(map(str, DFSPreorder(root)))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = data.split()
        def dfs():
            if nodes[cur_pos[0]] == 'None':
                cur_pos[0] += 1
                return None
            root = TreeNode(int(nodes[cur_pos[0]]))
            cur_pos[0] += 1
            root.left = dfs()
            root.right = dfs()
            return root
        cur_pos = [0]
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))