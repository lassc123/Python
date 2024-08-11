class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用
path = list[TreeNode]()
res = list[path]()
def pre_order(root:TreeNode):
    """前序遍历：例题二"""
    if root is None:
        return
    # 尝试
    path.append(root)
    if root.val == 7:
        # 记录解
        res.append(list[path])
    pre_order(root.left)
    pre_order(root.right)
    # 回退
    path.pop()