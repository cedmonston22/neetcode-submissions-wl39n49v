# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val:
            if self.isSameTree(root,subRoot):
                return True
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
        