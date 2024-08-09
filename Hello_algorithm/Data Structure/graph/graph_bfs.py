from graph_adjacency_list import GraphAdjList,Vertex
from collections import deque

def graph_bfs(graph:GraphAdjList,start_vet:Vertex)->list[Vertex]:
    """广度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希集合，用于记录已被访问过的顶点
    visited = set[Vertex]([start_vet])
    # 队列用于实现BFS
    que = deque[Vertex]([start_vet])
    # 以顶点vet为起点，循环直至访问完所有顶点
    while len(que)>0:
        vet = que.popleft()  # 队首顶点出队
        res.append(vet)      # 记录访问顶点
        # 遍历该顶点的所有邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue     # 跳过已被访问的顶点
            que.append(adj_vet) # 只入队为访问的顶点
            visited.add(adj_vet)# 标记该顶点已被访问
    # 返回顶点遍历序列
    return res

def dfs(graph:GraphAdjList,visited:set[Vertex],res:list[Vertex],vet:Vertex):
    """深度优先遍历辅助函数"""
    res.append(vet) # 记录访问顶点
    visited.add(vet) # 标记该顶点已被访问
    # 遍历该顶点的所有邻接顶点
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue  # 跳过已被访问的顶点
        # 递归访问邻接顶点
        dfs(graph,visited,res,adjVet)

def graph_dfs(graph:GraphAdjList,start_vet:Vertex)->list[Vertex]:
    """深度优先遍历"""
    # 使用邻接表来表示图，以便获取指定顶点的所有邻接顶点
    # 顶点遍历序列
    res = []
    # 哈希集合，用于记录已被访问果的顶点
    visited = set[Vertex]()
    dfs(graph,visited,res,start_vet)
    return res
