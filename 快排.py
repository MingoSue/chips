def qsort(array):
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    if len(array) < 2:
        return array
    else:
        # 递归条件
        pivot = array[0]
        # 由所有小于基准值的元素组成的子数组
        lesser = [i for i in array[1:] if i < pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i >= pivot]
        
        return qsort(lesser) + [pivot] + qsort(greater)

if __name__=='__main__':
    a = [5,6,78,9,0,-1,2,3,-65,12]
    print(qsort(a))
