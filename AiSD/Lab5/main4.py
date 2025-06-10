from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val= val;
        self.left = left;
        self.right = right;

root = TreeNode(val = "A")
root.left = TreeNode(val = "B")
root.right = TreeNode(val = "C")
root.left.left = TreeNode(val = "D")
root.left.right= TreeNode(val = "E")
root.right.left = TreeNode(val = "F")
root.right.right = TreeNode(val = "G")

# def bfs(root: TreeNode):
#      q = deque()# усторонний список
#      q += [root] # пока есть ноды
#      while q:
#         for _ in range(len(q)):
#             node = q.popleft() # идём в право
#             if node:
#                 print(node.val, end = " ")
#             q += [node.left]
#             q += [node.right]
def bfs(root: TreeNode):
    q = deque()
    q += [root]
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            if node:
                print(node.val, end=" ")
                q += [node.left] if node.left else []
                q += [node.right] if node.right else []
bfs(root)
