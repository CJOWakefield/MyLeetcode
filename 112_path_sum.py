# from collections import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return (self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val))
    
if __name__ == '__main__':

    def build_tree(arr, index=0):
        if index >= len(arr) or arr[index] is None:
            return None
        node = TreeNode(arr[index])
        node.left = build_tree(arr, 2 * index + 1)
        node.right = build_tree(arr, 2 * index + 2)
        return node
    
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    problem = Solution()
    print(problem.hasPathSum(root, 22))
