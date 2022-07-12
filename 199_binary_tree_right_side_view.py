# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        xs = [root]
        res = []
        while xs:
            res.append(xs[-1].val)
            _xs = []
            for x in xs:
                if x.left:
                    _xs.append(x.left)
                if x.right:
                    _xs.append(x.right)

            xs = _xs
        return res