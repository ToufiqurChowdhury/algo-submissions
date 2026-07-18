# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # algo: BFS
        # TC: O(n)
        # SC: O(1)

        res = []

        if not root:
            return []

        queue = [root]

        level = 0
        while queue:
            sublist = []
            qsize = len(queue)

            for i in range(qsize):
                node = queue.pop(0)
                sublist.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            level += 1
            if len(sublist) > 0:
                res.append(sublist)

        return res