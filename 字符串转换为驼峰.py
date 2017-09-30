
def to_string(istring, isplit):
    a = str(istring).split(isplit)
    c = []
    for i in a:
        c.append(i.capitalize())
    print(''.join(c))
    
# 调用
to_string('border-bottom-color', '-')
