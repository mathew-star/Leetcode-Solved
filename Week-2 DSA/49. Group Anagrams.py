from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res= defaultdict(list)
        for w in strs:
            key=''.join(sorted(w))
            res[key].append(w)
        return res.values()
        
            

                


        