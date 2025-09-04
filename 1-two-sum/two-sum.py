from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}  # value -> index
        n = len(nums)
        for i in range(n):             # no enumerate
            need = target - nums[i]
            if need in pos:
                return [pos[need], i]
            pos[nums[i]] = i
        return []  # or raise ValueError("No solution")
