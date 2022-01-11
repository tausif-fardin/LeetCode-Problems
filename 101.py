# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isMirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return (
                leftroot.val == rightroot.val
                and self.isMirror(leftroot.left, rightroot.right)
                and self.isMirror(leftroot.right, rightroot.left)
            )

        return leftroot == rightroot

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.isMirror(root.left, root.right)
