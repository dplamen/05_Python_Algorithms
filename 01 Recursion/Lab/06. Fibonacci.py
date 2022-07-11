# def fib_recursive(n):
#     if n <= 1:
#         return 1
#     return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n):
    fib0 = 1
    fib1 = 1
    result = 0
    for _ in range(n - 1):
        result = fib0 + fib1
        fib0, fib1 = fib1, result
    return result


number = int(input())
print(fib_iterative(number))
# print(fib_recursive(number))


