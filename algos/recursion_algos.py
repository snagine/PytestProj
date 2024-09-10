def fib_rec(n: int) -> list :
    if n <= 1:
        return n
    two_back = fib_rec(n - 2)
    one_back = fib_rec(n - 1)

    return one_back + two_back

fib = fib_rec(3)
# 0 1 1 2 3 5 8 13 21 34-> val
# 0 1 2 3 4 5 6  7  8  9-> index
# base cases : fib_rec(0) = 0, fib_rec(1) = 1
# fib_rec(2) = 1, fib_rec(3) = 2, fib_rec(4) = 3,  fib_rec(5) = 5, fib_rec(6) = 8
print(fib)