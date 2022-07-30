def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)

    print(node, sep=' ')


graph = [
    [3, 6],
    [2, 3, 4, 5, 6],
    [1, 4, 5],
    [0, 1, 5],
    [1, 2, 6],
    [1, 2, 3],
    [0, 1, 4]
]

visited = [False] * len(graph)

for node in range(len(graph)):
    dfs(node, graph, visited)
