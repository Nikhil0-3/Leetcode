class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result=[]
        l=len(nums)
        parts=l//3
        nums.sort()
        for i in range(0,l,3):
            if nums[i+2]-nums[i]<=k:
                result.append(nums[i:i+3])
            else:
                return []
        if len(result)==parts:
            return result



        