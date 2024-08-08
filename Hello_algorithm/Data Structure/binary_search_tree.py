class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用
class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self):
        """构造方法"""
        # 初始化空树
        self._root:TreeNode = None

    def search(self,num:int)->TreeNode|None:
        """查找节点"""
        cur  = self._root
        # 循环查找，越过叶节点后跳出
        while cur is not None:
            # 目标节点在cur的右子树中
            if cur.val<num:
                cur = cur.right
            # 目标节点出现在cur的左子树中
            elif cur.val>num:
                cur = cur.left
            # 找到目标节点，跳出循环
            else:
                break
        return cur