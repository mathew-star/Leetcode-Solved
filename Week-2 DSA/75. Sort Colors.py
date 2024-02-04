class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            c=i
            while c>0  and nums[c]< nums[c-1]:
                nums[c],nums[c-1]= nums[c-1],nums[c]
                c-=1
        return nums
        