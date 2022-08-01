def dfs(node, graph, visited, cycles):
    if node in cycles:
        raise Exception
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycles)

    cycles.remove(node)


graph = {}
while True:
    line = input()
    if line == "End":
        break
    parent, child = line.split('-')
    if parent not in graph:
        graph[parent] = []
    if child not in graph:
        graph[child] = []
    graph[parent].append(child)

visited = set()
cycles = set()
try:
    for node in graph:
        dfs(node, graph, visited, cycles)
    print('Acyclic: Yes')
except:
    print('Acyclic: No')

