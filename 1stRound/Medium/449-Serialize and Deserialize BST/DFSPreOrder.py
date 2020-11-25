# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def DFSPreorder(root):
            return [root.val] + DFSPreorder(root.left) + DFSPreorder(root.right)  if root else []
                
        return ' '.join(map(str, DFSPreorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if (data == ""):
            return None
        
        vals = [int(val) for val in data.split()]
        counter = 0
        
        def buildTree(minVal, maxVal):
            nonlocal counter
            if counter >= len(vals):
                return None
            if (vals[counter] < minVal or vals[counter] > maxVal):
                return None
            
            
            node = TreeNode(vals[counter])
            counter += 1
            node.left = buildTree(minVal, node.val)
            node.right = buildTree(node.val, maxVal)
            
            return node
        
        return buildTree(float("-inf"), float("inf"))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans