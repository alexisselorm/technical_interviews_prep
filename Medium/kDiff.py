from collections import Counter

nums = [1, 2, 3, 4, 4, 5, 6, 7, 3, 2, 8, 9]


def findPairs(nums, k: int) -> int:
    count = 0
    c = Counter(nums)
    if k == 0:
        for value in c.values():
            if value > 1:
                count += 1
    else:
        for key in c.keys():
            if key + k in c:
                count += 1
    return count


print(findPairs(nums, 0))
