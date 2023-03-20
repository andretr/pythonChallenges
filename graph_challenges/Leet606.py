# Definition for a binary tree node.
from graph_challenges.binaryTree import BinaryTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import Optional


class Solution:
    def tree2str(self, root: Optional[BinaryTree]) -> str:
        res = []

        def preorder(root):
            if not root:
                return
            res.append("(")
            res.append(str(root.val))

            preorder(root.left)
            preorder(root.right)

            res.append(")")
            return "".join(res)



if __name__ == '__main__':
    treenode = BinaryTree(1)
    treenode.insertLeft(2)
    treenode.insertLeft(4)
    treenode.insertRight(3)
    Solution.tree2str(treenode)
