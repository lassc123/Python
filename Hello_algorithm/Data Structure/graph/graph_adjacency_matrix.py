class GraphAdjMat:
    """基于邻接矩阵实现的无向图类"""

    def __init__(self,vertices:list[int],edges:list[list[int]]):
        """构造方法"""
        # 顶点列表，元素代表“顶点值”，索引代表“顶点索引”
        self.vertices:list[int] = []
        # 邻接矩阵，行列索引对应“顶点索引”
        self.adj_mat:list[list[int]] = []
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        # 请注意，edges元素代表顶点索引，即对应vertices元素索引
        for e in edges:
            self.add_edge(e[0],e[1])

    def size(self)->int:
        """获取顶点数量"""
        return len(self.vertices)
    
    def add_vertex(self,val:int):
        """添加顶点"""
        n = self.size()
        # 向顶点列表中添加新顶点的值
        self.vertices.append(val)
        # 在邻接矩阵中添加一行
        new_row = [0]*n
        self.adj_mat.append(new_row)
        # 在邻接矩阵中添加一列
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self,index:int):
        """删除顶点"""
        if index>=self.size():
            raise IndexError("越界访问")
        # 在顶点列表中移除索引index的顶点
        self.vertices.pop(index)
        # 在邻接矩阵中删除索引index的行
        self.adj_mat.pop(index)
        # 在邻接矩阵中删除索引index的列
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self,i:int,j:int):
        """添加边"""
        # 参数i,j对应vertices的元素索引
        # 索引越界与相等处理
        if i<0 or j<0 or i>=self.size() or j>=self.size() or i==j:
            raise IndexError()
        # 在无向图中，邻接矩阵关于主对角线对此，即满足（i，j） == （j,i）
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self,i:int,j:int):
        """删除边"""
        # 参数i,j对应vertices元素索引
        # 索引越界与相等处理
        if i<0 or j<0 or i>=self.size() or j>=self.size() or i==j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0
    
    def print_matrix(self):
        """打印邻接矩阵"""
        for row in self.adj_mat:
            print(row)


    def print(self):
        """打印邻接矩阵"""
        print("顶点列表=",self.vertices)
        print("邻接矩阵=")
        self.print_matrix()
    