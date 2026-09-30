def min_max(nums):
    if len(nums)==0: raise ValueError("Список не может быть пустым")
    min0=nums[0]
    for c in nums:
        if c<min0:min0=c
    max0=nums[0]
    for c in nums:
        if c>max0:max0=c
    return (min0,max0)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))