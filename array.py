def array(nums):
    res = 0
    nums.sort()
    for i in range(nums[0], nums[-1], 2):
        res += i
    return res


a = array([1, 4, 3, 2])
print a
