
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def function()-> int:
    """函数"""
    # 执行某些操作
    return 0

def constant(n:int)-> int:
    """常数阶"""
    # 常数，变量，对象占用O(1)空间
    a = 0
    nums = [0] * 10000
    node = ListNode()
    # 循环中的变量占用O（1）空间
    for _ in range(n):
        c = 0
    # 循环中的函数占用O(1) 空间
    for _ in range(n):
        function()

def linear(n:int):
    """线性阶"""
    # 长度为n的列表占用O(N)空间
    nums =[0] * n
    # 长度为n的哈希表占用O(n)空间
    hmap = dict[int,str]()
    for i in range(n):
        hmap[i] = str(i)

def linear_recur(n:int):
    """线性阶（递归实现）"""
    print("递归 n=",n)
    if n == 1:
        return
    linear_recur(n-1)

def quadratic(n:int)-> int:
    """平方阶"""
    # 二维列表占用O(n^2)空间
    num_matrix = [[0]*n for _ in range(n)]

def quadratic_recur(n:int)->int:
    """平方阶（递归实现）"""
    if n <= 0:
        return 0
    # 数组 nums 长度为n，n-1，。。。，2，1
    nums =[0]*n
    return quadratic_recur(n-1)

def build_tree(n:int)-> TreeNode|None:
    """指数阶（建立满二叉树）"""
    if n == 0:
        return None
    root =TreeNode(0)
    root.left = build_tree(n-1)
    root.right = build_tree(n-1)
    return root