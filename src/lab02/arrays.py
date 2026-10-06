def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Вернуть (минимум, максимум). Пустой список -> ValueError."""
    if len(nums) == 0:
        raise ValueError("Список пуст")
 
    lo = hi = nums[0]
    for x in nums[1:]:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return (lo, hi)
print(min_max([1.5, 2, 2.0, -3.1]))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    sp=list(set(nums))
    for i in range(len(sp) - 1):          
        for j in range(len(sp) - 1 - i):  
            if sp[j] > sp[j + 1]:
                sp[j], sp[j + 1] = sp[j + 1], sp[j]
    return sp


def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"Ожидался list или tuple, получено {type(row).__name__}")
        for x in row:
            result.append(x)
    return result
