from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        res = []
        def parse(traversal):
            i = 0
            while i < len(traversal):
                depth, val = 0, 0
                while i < len(traversal) and traversal[i] == '-':
                    depth += 1
                    i += 1
                while i < len(traversal) and traversal[i].isdigit():
                    val = (val * 10) + int(traversal[i])
                    i += 1
                res.append((depth, val))

        def traverse_parsing(res):
            stack = []
            for depth, val in res:
                node = TreeNode(val)
                while len(stack) > depth: stack.pop()
                if stack:
                    if stack[-1].left is None: stack[-1].left = node
                    else: stack[-1].right = node
                stack.append(node)
            return stack[0]
        
        parse(traversal)
        return traverse_parsing(res)

    def print_tree(self, root: TreeNode, level: int = 0, prefix: str = "Root: "):
        if not root: return
        print("  " * level + prefix + str(root.val))
        if root.left:
            self.print_tree(root.left, level + 1, "L--- ")
        if root.right:
            self.print_tree(root.right, level + 1, "R--- ")

## Notes for self:
# Intuition:
# - Parse the traversal string into a list of tuples, where each tuple contains the depth and value of the node.
# - Traverse the list and construct the tree.
# - Use a stack to keep track of the nodes.
# - Remove from the stack until we reach the current depth.
# - Add the current node as a left child if there is space, otherwise add it as a right child.
# - Return the root of the tree.


if __name__ == "__main__":
    problem = Solution()
    print(problem.print_tree(problem.recoverFromPreorder("1-2--3--4-5--6--7")))
    print(problem.print_tree(problem.recoverFromPreorder("1-401--349---90--88")))