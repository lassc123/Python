class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用

res = list[TreeNode]
def pre_order(root:TreeNode):
    """前序遍历：例题一"""
    if root is None:
        return
    if root.val == 7:
        # 记录解
        res.append(root)
    pre_order(root.left)
    pre_order(root.right)