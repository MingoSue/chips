# 阶乘factorial
def fac(n):
    if n < 2:
        return 1
    return n * fac(n-1)

# 调用
a = int(input('an integer number:\n' ))
print(fac(a))

