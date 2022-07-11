def sum_array(arr, idx=0):
    if idx == len(arr) - 1:
        return arr[idx]
    return arr[idx] + sum_array(arr, idx + 1)


numbers = [int(x) for x in input().split()]
print(sum_array(numbers))
