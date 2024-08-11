def move(src:list[int],tar:list[int]):
    """移动一个圆盘"""
    # 从src顶部拿出一个圆盘
    pan = src.pop()
    # 将圆盘放入tar顶部
    tar.append(pan)

def dfs(i:int,src:list[int],buf:list[int],tar:list[int]):
    """求解汉诺塔问题f（i）"""
    # 若src只剩下一个圆盘，则可以直接将其移到tar
    if i == 1:
        move(src,tar)
        return
    # 子问题f（i-1）：将src顶部n-1个圆盘借助tar移到buf
    dfs(i-1,src,tar,buf)
    # 子问题f（1）:将src剩余一个圆盘移到tar
    move(str,tar)
    # 子问题f（i-1）:将buf顶部i-1个圆盘借助src移到tar
    dfs(i-1,buf,src,tar)

def solve_hanota(A:list[int],B:list[int],C:list[int]):
    """求解汉诺塔问题"""
    n = len(A)
    # 将A顶部n个圆盘借助B移到C
    dfs(n,A,B,C)