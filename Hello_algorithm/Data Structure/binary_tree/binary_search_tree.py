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
    
    def insert(self,num:int):
        """插入节点"""
        # 若树为空，则初始化根节点
        if self._root is None:
            self._root = TreeNode(num)
            return
        # 循环查找，越过叶节点后跳出
        cur,pre = self._root,None
        while cur is not None:
            # 找到重复节点，直接返回
            if cur.val == num:
                return
            pre = cur
            # 插入位置在cur的右子树中
            if cur.val<num:
                cur = cur.right
            # 插入位置在cur的左子树中
            else:
                cur = cur.left
        # 插入节点
        node  = TreeNode(num)
        if pre.val<num:
            pre.right = node
        else:
            pre.left = node

    def remove(self,num:int):
        """删除节点"""
        # 若树为空，直接提前返回
        if self._root is None:
            return
        # 循环查找，越过叶节点后跳出
        cur,pre = self._root,None
        while cur is not None:
            # 找到待删除节点，跳出循环
            if cur.val == num:
                break
            pre =cur
            # 待删除节点在cur的右子树中
            if cur.val<num:
                cur = cur.right
            # 待删除节点在cur的右子树中
            else:
                cur = cur.left
        # 若无待删除节点，则直接返回
        if cur is None:
            return
        
        # 子节点数量 = 0 or 1
        if cur.left is None or cur.right is None:
            # 当子节点数量 = 0/1时，child = null/该子节点
            child = cur.left or cur.right
            # 删除节点cur
            if cur != self._root:
                if pre.left == cur:
                    pre.left = child
                else:
                    pre.right = child
            else:
                # 若删除节点为根节点，则重新指定根节点
                self._root = child
        # 子节点数量 = 2
        else:
            # 获取中序遍历中cur的下一个节点
            tmp:TreeNode = cur.right
            while tmp.left is not None:
                tmp = tmp.left
            # 递归删除节点tmp
            self.remove(tmp.val)
            # 用tmp覆盖cur
            cur.val = tmp.val