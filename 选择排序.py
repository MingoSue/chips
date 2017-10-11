# 先编写一个用于找出数组中最小元素的函数
def findSmallest(arr):
    # 存储最小的值
    smallest = arr[0]
    # 存储最小元素的索引
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 对数组进行排序
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # 找出数组中最小的元素，并将其加入到新数组中
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

# 调用
print(selectionSort([5, 3, 6, 2, 10]))
