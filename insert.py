# 插入排序
def insert_sort(lists):
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

# 调用
a = [1,2,3,7,5,4]
print(insert_sort(a))
