def for_loop(n:int)->int:
    """for循环"""
    res=0
    # 循环求和 1，2，......,n-1,n
    for i in range(1,n+1):
        res += i
    return res

def while_loop(n:int)->int:
    """while循环"""
    res=0
    i=1# 初始化条件变量
    # 循环求和1，2，......,n-1,n
    while i<=n:
        res+=i
        i+=1 # 更新条件变量
    return res

def while_loopii(n:int)->int:
    """while循环（两次更新）"""
    res=0
    i=1 # 初始化条件变量
    while i<=n:
        # 循环求和1，4，10，......
        res+=i
        # 更新条件变量
        i+=1
        i*=2
    return res

def nested_for_loop(n:int)->str:
    """双层for循环"""
    res=""
    # 循环i=1，2,3,......,n-1,n
    for i in range(1,n+1):
        # 循环j=1,2,......,n-1,n
        for j in range(1,n+1):
            res+=f"({i},{j}),"
    return res