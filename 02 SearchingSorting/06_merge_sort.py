def merge_arrays(left, right):
    sorted_arr = []
    left_idx = 0
    right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_arr.append(left[left_idx])
            left_idx += 1
        else:
            sorted_arr.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        sorted_arr.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        sorted_arr.append(right[right_idx])
        right_idx += 1

    return sorted_arr


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid_idx = len(arr) // 2
    left = arr[:mid_idx]
    right = arr[mid_idx:]
    return merge_arrays(merge_sort(left), merge_sort(right))


lst = [int(x) for x in input().split()]
result = merge_sort(lst)
print(*result, sep=' ')
