from collections import Counter
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> TreeNode:
        self.counter = Counter()
        self.results = []

        self.dfs(root)

        return self.results

    def dfs(self, root):
        if not root:
            return "#"

        serial = "{},{},{}".format(
            root.val, self.dfs(root.left), self.dfs(root.right))

        self.counter[serial] += 1
        if self.counter[serial] == 2:
            self.results.append(root)

        return serial
