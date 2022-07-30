from collections import deque
queue = deque()


def bds(node, graph, visited):
    if node in visited:
        return

    visited.add(node)
    queue.append(node)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        for child in graph[current_node]:
            if child not in visited:
                visited.add(child)
                queue.append(child)


graph = {
    7: [19, 21, 14],
    19: [1, 12, 31, 21],
    1: [7],
    12: [],
    31: [21],
    21: [14],
    14: [6, 23],
    23: [21],
    6: []
}

visited = set()
bds(7, graph, visited)
