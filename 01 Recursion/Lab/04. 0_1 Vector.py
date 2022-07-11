def gen01(idx, v):
    if idx >= len(v):
        print(*v, sep='')
        return
    for num in range(2):
        v[idx] = num
        gen01(idx + 1, v)


n = int(input())
vector = [None] * n
gen01(0, vector)
