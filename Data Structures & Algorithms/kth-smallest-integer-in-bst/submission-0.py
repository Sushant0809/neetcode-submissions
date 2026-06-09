# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k
        self.ans = 0

        def check_small(root):

            if not root:
                return 
            
            check_small(root.left)
            self.k-=1
            if self.k == 0:
                self.ans = root.val

            if self.k>0:
                check_small(root.right)
        
        check_small(root)
        return self.ans

           

            



        