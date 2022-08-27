from collections import deque


def find_path(parent, node):
    path = deque()
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    return path


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

source = int(input())
destination = int(input())

distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)
distance[source] = 0

for _ in range(nodes - 1):
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            parent[second] = first

for first, second, weight in graph:
     new_distance = distance[first] + weight
     if new_distance < distance[second]:
        print('Undefined')
        break
else:
   path = find_path(parent, destination)
   print(*path, sep=' ')
   print(distance[destination])
