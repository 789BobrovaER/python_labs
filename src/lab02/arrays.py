def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("Список пуст")
 
    lo = hi = nums[0]
    for x in nums[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return (lo, hi)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''Вернуть отсортированный список уникальных значений (по возрастанию).'''
    sp=list(set(nums))
    for i in range(len(sp) - 1):          
        for j in range(len(sp) - 1 - i):  
            if sp[j] > sp[j + 1]:
                sp[j], sp[j + 1] = sp[j + 1], sp[j]
    return sp


def flatten(mat: list[list | tuple]) -> list:
    '''«Расплющить» список списков/кортежей в один список по строкам (row-major). \
        Если встретилась строка/элемент, который не является списком/кортежем — TypeError.'''
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Ожидался list или tuple, получено {type(row).__name__}")
        for x in row:
            result.append(x)
    return result
<<<<<<< HEAD
=======
print(flatten([[1], [], [2, 3]]))
>>>>>>> 1a3b282a99cc590ac79a3c1f328dd9183ebae6c4
