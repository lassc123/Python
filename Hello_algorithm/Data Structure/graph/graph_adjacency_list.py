class Vertex:
    """顶点类"""
    def __init__(self, val: int):
        self.val = val
    def vals_to_vets(vals: list[int]) -> list["Vertex"]:
        """输入值列表 vals ，返回顶点列表 vets"""
        return [Vertex(val) for val in vals]

class GraphAdjList:
    """基于邻接表实现的无向图类"""

    def __init__(self,edges:list[list[Vertex]]):
        """构造方法"""
        # 邻接表，key:顶点，value:该顶点的所有邻接顶点
        self.adj_list = dict[Vertex,list[Vertex]]()
        # 添加所有顶点和边
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0],edge[1])

    def size(self)->int:
        """获取顶点数量"""
        return len(self.adj_list)
    

    def add_edge(self,vet1:Vertex,vet2:Vertex):
        """添加边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1==vet2:
            raise ValueError()
        # 添加边vet1 - vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self,vet1:Vertex,vet2:Vertex):
        """删除边"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1==vet2:
            raise ValueError()
        # 删除边vet1-vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self,vet:Vertex):
        """添加顶点"""
        if vet in self.adj_list:
            return
        # 在邻接表中添加一个新链表
        self.adj_list[vet] = []

    def remove_vertex(self,vet:Vertex):
        """删除顶点"""
        if vet not in self.adj_list:
            raise ValueError()
        # 在邻接表中删除顶点vet对应的链表
        self.adj_list.pop(vet)
        # 遍历其他顶点的链表，删除所有包含vet的边
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def print(self):
        """打印邻接表"""
        print("邻接表=")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}:{tmp},")