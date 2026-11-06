# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root: 
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #Tổng lớn nhất nếu đường đi bẻ cong qua node hiện tại
            res[0] = max(res[0], root.val + leftMax + rightMax)
            #cập nhật Tổng lớn nhất của đường đi chỉ đi theo một hướng
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]