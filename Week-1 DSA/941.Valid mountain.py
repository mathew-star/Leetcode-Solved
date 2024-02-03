"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

Strictly increasing and strictly decreasing

Approach>> used two variables>> st_dec and st_in to track if strictly increasing and decreasing 
when the loop stops where it can't find any more increasing numbers the a function strict_dec will run with the current i and array as the arguments and check if the rest is strictly decresing
"""
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        st_dec = None
        st_in = None
        
        def strict_dec(arr, k):
            for i in range(k, len(arr) - 1):
                if arr[i + 1] < arr[i]:
                    continue
                else:
                    return False
            return True

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                st_in = True
            else:
                st_dec = strict_dec(arr, i - 1)
                break

        if st_dec and st_in:
            return True
        else:
            return False


