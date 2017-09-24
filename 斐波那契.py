
def fib(n):
    if n <= 2 and n >= 0:
        return 1
    return fib(n-1)+fib(n-2)

n = int(input('input a number:'))
print(fib(n))

def fib_li(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib_li(n))
