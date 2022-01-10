# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node):
            if not node:
                return
            traversal.append(node.val)
            preorder(node.left)
            preorder(node.right)
            return traversal

        traversal = []
        return preorder(root)
