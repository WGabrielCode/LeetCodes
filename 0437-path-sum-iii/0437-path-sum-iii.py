# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        result = 0
        visited_starts = set()

        def rec(node, curr_sum):
            nonlocal result

            new_sum = curr_sum + node.val
            if new_sum == targetSum:
                result += 1

            if node.left:
                rec(node.left, new_sum)
            if node.right:
                rec(node.right, new_sum)

            if node.left and id(node.left) not in visited_starts:
                visited_starts.add(id(node.left))
                rec(node.left, 0)

            if node.right and id(node.right) not in visited_starts:
                visited_starts.add(id(node.right))
                rec(node.right, 0)

        visited_starts.add(id(root))
        rec(root, 0)

        return result
