import collections
class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class TreeAlgos:

    def verticalOrder2(self, root: TreeNode) -> list[list[int]]:
        if root is None:
            return []

        queue = [(root, 0)]
        cols = {}

        while queue:
            node, col = queue.pop(0)
            if col in cols:
                cols[col].append(node.val)
            else:
                cols[col] = [node.val]
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        low = min(cols.keys())
        high = max(cols.keys())
        ans = []

        for i in range(low, high + 1):
            ans.append(cols[i])

        return ans

        columns = {}
        queue = [(root, 0)]
        while len(queue):
            node, col = queue.pop(0)
            if col in columns:
                columns[col].append(node.val)
            else:
                columns[col] = [node.val]

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        low = min(columns.keys())  # O(len(columns))
        high = max(columns.keys())  # O(len(columns))
        order = []
        for i in range(low, high + 1):  # O(len(2 * dept - 1)) < O(len(columns))
            order.append(columns[i])  # O(1)

        return order

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, curr):
            if not node:
                return False

            # if both children are null, then the node is a leaf
            if node.left == None and node.right == None:
                return (curr + node.val) == targetSum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right

        return dfs(root, 0)

    def preorder_dfs(self, node: TreeNode):
        if not node:
            return

        print(node.val)
        self.preorder_dfs(node.left)
        self.preorder_dfs(node.right)
        return

    def minDepthRec(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0

        left = self.minDepthRec(root.left)
        right = self.minDepthRec(root.right)
        return min(left, right) + 1

    def maxDepthRec(self, root: TreeNode) -> int:
        if not root:
            return 0

        left = self.maxDepthRec(root.left)
        right = self.maxDepthRec(root.right)
        return max(left, right) + 1

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 1)] # LIFO
        ans = 0

        while stack:
            node, depth = stack.pop()
            ans = max(ans, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return ans

tree_algos = TreeAlgos()
# root = TreeNode(0)
# one = TreeNode(1)
# two = TreeNode(2)
# three = TreeNode(3)
# four = TreeNode(4)
# five = TreeNode(5)
# six = TreeNode(6)
#
# root.left = one
# root.right = two
# one.left = three
# one.right = four
# two.right = five
# five.right = six

# print(tree_algos.maxDepth(root))
# print(tree_algos.maxDepthRec(root))
# print(tree_algos.hasPathSum(root, 5))

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
# build tree
root_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
node_6 = TreeNode(6)
root_2.right = node_3
node_3.right = node_4
node_4.right = node_5
node_5.right = node_6

# print(tree_algos.minDepthRec(root))


# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = collections.defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# print(sorted(d.items()))
# print(d.keys())
# print(d.values())
# print(d)
l = [3,9,20,None,None,15,7]
root = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

root.left = nine
root.right = twenty
twenty.left = fifteen
twenty.right = seven

# res = tree_algos.verticalOrder(root)
res = tree_algos.verticalOrder2(root)
print(res)
