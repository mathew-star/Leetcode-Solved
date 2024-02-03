"""
1239. Maximum Length of a Concatenated String with Unique Characters
Solved
Medium
Topics
Companies
Hint
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.


        Approach:
        - Utilizes a backtracking approach to explore all possible combinations of strings.
        - The 'checkunique' function ensures that only valid combinations (with unique characters) are considered.
        - The 'backtrack' function is a recursive function that explores both inclusion and exclusion of each string.
        - The base case is when the end of the array is reached, at which point the length of the current string is returned.
        - The function returns the maximum length encountered during the exploration.

"""
class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def checkunique(s):
            return len(set(s)) == len(s)

        def backtrack(index, current_str):
            if index == len(arr):
                return len(current_str)


            # Include the current string
            include_length = 0
            if checkunique(current_str + arr[index]):
                include_length = backtrack(index + 1, current_str + arr[index])

            # Exclude the current string
            exclude_length = backtrack(index + 1, current_str)

            return max(include_length, exclude_length)

        return backtrack(0, "")
