# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #recursive solution
        
        if not p and not q: #if the tree is empty (null)
            return True
        if not p or not q or p.val != q.val: #only one of them is null, value of p and value of q is not same
            return False
        
        return (self.isSameTree(p.right, q.right) and
                self.isSameTree(p.left, q.left))