def fib5(n: int) -> int:
    if n == 0:
        return n  # специальный случай
    last: int = 0  # начальное значение fib(0)
    next: int = 1  # начальное значение fib(1)

    for m in range(1, n):
        # хитрая распаковка кортежа
        last, next = next, last + next
    return next


print(fib5(2))
print(fib5(51))

# 0 1 1 2 3 5 8 ...
