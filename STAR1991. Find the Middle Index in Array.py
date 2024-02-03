



class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot_sum=sum(nums)
        l_sum=0
        for i in range(len(nums)):
            tot_sum -= nums[i]
            if l_sum == tot_sum:
                return i
            l_sum += nums[i]

        return -1
        



