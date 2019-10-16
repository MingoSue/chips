# 生成器next()和send()方法示例
def gen(max):
    base = 0
    i = 0
    while i < max:
        print('base: ', base)
        o = (yield base + i )

        if o is not None:
            print('ooooo', o)
            base = o
        else:
            i += 1
            print('iiiii', i)


#if __name__ == '__main__':
g = gen(10)
print('next: ', next(g), '\n')
print('next: ', next(g), '\n')

print('send: ', g.send(10), '\n')
print('next: ', next(g))