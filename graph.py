graph = {
    "a": ['b','c'],
    "b": ['a','c','d'],
    "c": ['a','b','d','e'],
    "d": ['b','c','e','f'],
    "e": ['c','d'],
    "f": ['d']
}
print("广度优先遍历")
def BFS (graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)
BFS(graph,"f")
print("深度优先遍历,非递归")
def DFS (graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue) > 0:
        vertex = queue.pop()
        nodes = graph[vertex]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(vertex)
DFS(graph,"f")
print ("深度优先遍历，递归写法")
seen = set()
def recursion_DFS (graph,start):
    if start not in seen:
        print(start)
        seen.add(start)
    for node in graph[start]:
        if node not in seen:
            recursion_DFS (graph,node)
recursion_DFS (graph,"f")
