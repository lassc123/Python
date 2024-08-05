import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活跃状态，就不断地模拟随机漫步
while True:
        # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    # 创建新的图形
    plt.figure(figsize=(10,6))
    point_numbers=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    # 突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    # 隐藏坐标轴
    plt.axis('off')
    # 设置绘图区域的范围
    plt.xlim(min(rw.x_values),max(rw.x_values))
    plt.ylim(min(rw.y_values),max(rw.y_values))
    plt.tight_layout()
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n': 
        break