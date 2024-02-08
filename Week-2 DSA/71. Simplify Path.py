        
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack=[]
        splited=path.split("/")
        print(splited)
        for i in splited:
            print(path_stack)
            if path_stack and i == "..":
                path_stack.pop()
            elif i=="." or i=="" or i=="..":
                continue
            else:
                path_stack.append(i)
        return "/" +  "/".join(path_stack)