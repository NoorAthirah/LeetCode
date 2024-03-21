# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        
        while stack: #node is not empty, loop until node is empty
            node, depth = stack.pop() #stack.pop - Deletes the topmost element of the stack – Time Complexity: O(1)
            
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return res
    
    #append() is used to add elements to the top of the stack while pop() removes the element in LIFO orde
        