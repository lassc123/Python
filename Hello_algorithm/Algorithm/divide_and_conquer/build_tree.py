class TreeNode:
    """二叉树节点类"""
    def __init__(self,val:int):
        self.val = val                   # 节点值
        self.left:TreeNode|None = None   # 左节点引用
        self.right:TreeNode|None = None  # 右节点引用
def dfs(preorder:list[int],inorder_map:dict[int],i:int,l:int,r:int)->TreeNode|None:
    """构建二叉树：分治"""
    # 子树区间为空时终止
    if r-l < 0:
        return None
    # 初始化根节点
    root = TreeNode(preorder[i])
    # 查询m，从而划分左右子树
    m = inorder_map[preorder[i]]
    # 子问题：构建左子树
    root.left = dfs(preorder,inorder_map,i+1,l,m-1)
    # 子问题：构建右子树
    root.right = dfs(preorder,inorder_map,i+1+m-l,m+1,r)

def build_tree(preorder:list[int],inorder:list[int])->TreeNode|None:
    """构建二叉树"""
    # 初始化哈希表，存储inorder元素到索引的映射
    inorder_map = {val: i for i,val,in enumerate(inorder)}
    root = dfs(preorder,inorder_map,0,0,len(inorder)-1)
    return root