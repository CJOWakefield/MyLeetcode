class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def symmetric(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False

            l_symmetry = symmetric(node1.left, node2.right)
            r_symmetry = symmetric(node1.right, node2.left)
            return node1.val == node2.val and l_symmetry and r_symmetry

        return symmetric(root.left, root.right)
    
if __name__ == "__main__":
    problem = Solution()
    print(problem.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
    print(problem.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))))
    