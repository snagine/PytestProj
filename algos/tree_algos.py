import collections
class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class TreeAlgos:
    def preorder_dfs(self, node: TreeNode):
        if not node:
            return

        print(node.val)
        self.preorder_dfs(node.left)
        self.preorder_dfs(node.right)
        return

tree_algos = TreeAlgos()
root = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)

root.left = one
root.right = two

print(root.left.val)
print(root.right.val)
