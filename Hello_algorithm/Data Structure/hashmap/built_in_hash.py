num = 3
hash_num = hash(num)
# 整数3的哈希值为3

bol = True
hash_bol = hash(bool)
# 布尔量True的哈希值为1

dec = 3.14159
hash_dec = hash(dec)
# 小数3.14159的哈希值为32648311674566659

str = "Hello 算法"
hash_str = hash(str)
# 字符串"Hello 算法"的哈希值为4617003410720528961

tup = (12836,"小哈")
hash_tup = hash(tup)
# 元组(12836，"小哈")的哈希值为1029005403108185979

class ListNode:
    """单链表节点类"""
    def __init__(self,val:int):
        self.val:int = val              # 节点值
        self.next: ListNode|None =None  # 指向下一节点的引用

obj = ListNode(0)
hash_obj = hash(obj)
# 节点对象<ListNode object at 0x1058fd810>的哈希值为274267521