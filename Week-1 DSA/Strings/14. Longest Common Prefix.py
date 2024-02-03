class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)== 1:
            return strs[0]
            
        def comman(s1,s2):
            res=""
            i,j=0,0
            n1,n2=len(s1),len(s2)
            print(s1,s2)
            while i<= n1-1 and j<=n2-1:
                if s1[i] != s2[j]:
                    break
                print(s1[i],s2[j])
                res+= s1[i]
                i,j=i+1,j+1
            return res

        prefix= strs[0]
        for i in range(1,len(strs)):
            prefix = comman(prefix,strs[i])
        return prefix
        
"""
Binary search approach>>
"""  
strs =\
["flower","flow","flight"]
def prefix(strs):
    if not strs:
        return ""
    min_str= min(strs,key=len)
    l=0
    h=len(min_str)-1
    while l<=h:
        mid = (l + h) //2
        if all(s.startswith(min_str[:mid+1]) for s in strs):
            l= mid+1
        else:
            h= mid-1
    return min_str[:l]
