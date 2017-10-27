def digits(num):
    if num < 10 :
        return num
    else :
        return 1 + (num-1)%9

a = digits(38)
print a
