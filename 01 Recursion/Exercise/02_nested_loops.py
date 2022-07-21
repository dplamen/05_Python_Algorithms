def nested_loop(idx, v):
    if idx == len(v):
        print(*v, sep=' ')
        return
    for i in range(1, len(v) + 1):
        v[idx] = i
        nested_loop(idx + 1, v)


n = int(input())
vector = [None] * n
nested_loop(0, vector)
