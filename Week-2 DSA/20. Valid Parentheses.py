class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_parenth=[]
        parthis_map={')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parthis_map:
                if open_parenth and parthis_map[c] == open_parenth[-1]:
                    open_parenth.pop()
                else:
                    return False
            else:
                c.append(c)
        return True if not open_parenth else False