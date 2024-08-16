import math
def max_product_cutting(n:int)->int:
    """最大切分乘积：贪心"""
    # 当n<=3时，必须切分出一个1
    if n <= 3:
        return 1*(n-1)
    # 贪心地切分出3，a为3的个数，b为余数
    a,b = n//3,n%3
    if b == 1:
        # 当余数为1时，将一对1*3转化为2*2
        return int(math.pow(3,a-1))*2*2
    if b == 2:
        # 当余数为2时，不做处理
        return int(math.pow(3,a))*2
    # 当余数为0时，不做处理
    return int(math.pow(3,a))