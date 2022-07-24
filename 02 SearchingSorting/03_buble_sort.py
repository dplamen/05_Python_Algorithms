nums = [int(x) for x in input().split()]

is_sorted = False
i = 0

while not is_sorted:
    is_sorted = True
    for idx in range(len(nums) - 1 - i):
        if nums[idx] > nums[idx + 1]:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]
            is_sorted = False

    i += 1

print(*nums, sep=' ')
