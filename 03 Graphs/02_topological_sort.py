def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0
        for child in children:
            if child not in result:
                result[child] = 1
            else:
                result[child] += 1
    return result


def find_node_no_dependency(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node
    return None


nodes = int(input())
graph = {}

for _ in range(nodes):
    line = input().split('->')
    node = line[0].strip()
    children = line[1].strip().split(', ') if line[1] else []
    graph[node] = children

dependencies_by_node = find_dependencies(graph)
has_cycles = False
sorted_graph = []

while dependencies_by_node:
    node_to_remove = find_node_no_dependency(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_graph.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_graph)}")




