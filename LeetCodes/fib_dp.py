def fib(n):
    if n <= 1:
        return n
    x = fib(n - 1)
    y = fib(n - 2)

    return x + y

n = int(input())
print(fib(n))