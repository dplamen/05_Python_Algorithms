def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot, left, right = start, start + 1, end
    while left <= right:
        if arr[left] > arr[pivot] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[left] <= arr[pivot]:
            left += 1
        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


lst = [int(x) for x in input().split()]
quick_sort(lst, 0, len(lst) - 1)
print(*lst, sep=' ')
