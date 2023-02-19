# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        level = 1
        reverse = False
        while queue:
            level_values = []
            for i in range(len(queue)):
                node = queue.pop(0)
                level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if reverse:
                level_values.reverse()
            result.append(level_values)
            level = 1 - level
            reverse = not reverse
        return result



