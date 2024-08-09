class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用

# 初始化二叉树
# 初始化节点
n1 = TreeNode(val=1)
n2 = TreeNode(val=2)
n3 = TreeNode(val=3)
n4 = TreeNode(val=4)
n5 = TreeNode(val=5)
# 构造节点之间的引用（指针）
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
# 插入与删除节点
p =TreeNode(0)
# 在n1->n2中间插入节点P
n1.left = p
p.left = n2
# 删除节点
n1.left = n2
