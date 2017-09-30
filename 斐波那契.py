# 输出第n项的值
def fib(n):
    if n <= 2 and n >= 0:
        return 1
    return fib(n-1)+fib(n-2)
# 输出列表
def fib_li(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
# 执行
n = int(input('input a number:'))
print(fib(n))
print(fib_li(n))

