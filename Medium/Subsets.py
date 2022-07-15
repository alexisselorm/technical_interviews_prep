

class Solution:
    def subsets(self, nums):
        numset =[[]]
        for num in nums:
            numset += [lst +[num] for lst in numset ]
        return numset

