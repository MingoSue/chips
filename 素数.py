'''l = []
for i in range(101,200):
    for j in range(2,i-1):
        if i%j ==0:
            break
    else:
        l.append(i)

print(l)

print("总数为：%d" % len(l))
'''
s = []
for i in range(101, 200):
    count = 0
    for j in range(1, i+1):
        if (i % j) == 0:
            count += 1
    if count == 2:
        s.append(i)
print(s, '\n共有%s个素数'%len(s))
