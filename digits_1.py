def digits(num):
    while num/10 > 0 :
        sum = 0
        while num != 0 :
            sum += num % 10
            num = num / 10
        num = sum
    return num

a = digits(38)
print a
