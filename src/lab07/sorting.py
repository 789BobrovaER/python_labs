def bubble_sort(nums) -> list:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    nums2 = list(nums)
    n = len(nums2)
    for i in range(n):
        changed = False
        for j in range(n - i - 1):
            if nums2[j] > nums2[j + 1]:
                nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]
                changed = True
        if not changed:  # обменов не было — список уже отсортирован
            break
    return nums2


def selection_sort(nums) -> list:
    """Тот же контракт, что у bubble_sort."""
    nums2 = list(nums)
    n = len(nums2)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if nums2[j] < nums2[min_pos]:
                min_pos = j
        if min_pos != i:
            nums2[i], nums2[min_pos] = nums2[min_pos], nums2[i]
    return nums2


def insertion_sort(nums) -> list:
    """Тот же контракт, что у bubble_sort."""
    nums2 = list(nums)
    for i in range(1, len(nums2)):
        t = nums2[i]
        j = i
        while j > 0 and nums2[j - 1] > t:
            nums2[j] = nums2[j - 1]
            j -= 1
        nums2[j] = t
    return nums2