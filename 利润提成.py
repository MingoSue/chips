pro = input('利润：')
lis = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.07, 0.1]
r = 0

for i in range(len(lis)):
    if int(pro) > lis[i]:
        r += (int(pro)-lis[i])*rat[i]
        print(round((int(pro)-lis[i])*rat[i],1))
        pro = lis[i]
print(round(r,1))
