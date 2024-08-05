class ListNode:
    """单链表节点类"""
    def __init__(self,val:int):
        self.val:int = val              # 节点值
        self.next: ListNode|None =None  # 指向下一节点的引用
# class ListNode:
#     """双向链表节点类"""
#     def __init__(self, val: int):
#         self.val: int = val                # 节点值
#         self.next: ListNode | None = None  # 指向后继节点的引用
#         self.prev: ListNode | None = None  # 指向前驱节点的引用
# 初始化链表1->3->2->5->4
# 初始化各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)
# 构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4

def insert(n0:ListNode,P:ListNode):
    """在链表的节点n0之后插入节点P"""
    n1 = n0.next
    P.next = n1
    n0.next = P

def remove(n0:ListNode):
    """删除链表的节点n0之后的首个节点"""
    if not n0.next:
        return
    # n0->P->n1
    P = n0.next
    n1 = P.next
    n0.next = n1

def access(head:ListNode,index:int)->ListNode|None:
    """访问链表中索引为index的节点"""
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

def find(head:ListNode,target:int)->int:
    """在链表中查找值为target的首个节点"""
    index = 0
    while head:
        if head.val ==target:
            return index
        head = head.next
        index += 1
    return -1
