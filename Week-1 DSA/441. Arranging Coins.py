



class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
         
        k = 1 
        total_coins = 0
        
        while total_coins + k <= n:
            total_coins += k
            k += 1

        return k - 1