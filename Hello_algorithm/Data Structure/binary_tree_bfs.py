from collections import deque
class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用

def level_order(root:TreeNode|None)->list[int]:
    """层序遍历"""
    # 初始化队列，加入根节点
    queue:deque[TreeNode] =deque()
    queue.append(root)
    # 初始化一个列表，用于保存遍历序列
    res = []
    while queue:
        node:TreeNode = queue.popleft() # 队列出队
        res.append(node.val) # 保存节点值
        if node.left is not None:
            queue.append(node.left)  # 左子节点入队
        if node.right is not None:
            queue.append(node.right) # 右子节点入队
        return res

def pre_order(root:TreeNode|None,res:list):
    """前序遍历"""
    if root is None:
        return
    # 访问优先级：根节点->左子树->右子树
    res.append(root.val)
    pre_order(root.left,res)
    pre_order(root.right,res)

def in_order(root:TreeNode|None,res:list):
    """中序遍历"""
    if root is None:
        return
    # 访问优先级：左子树->根节点->右子树
    in_order(root.left,res)
    res.append(root.val)
    in_order(root.right,res)

def post_order(root:TreeNode|None,res:list):
    """后序遍历"""
    if root is None:
        return
    # 访问优先级：左子树->右子树->根节点
    in_order(root.left,res)

    in_order(root.right,res)
    res.append(root.val)