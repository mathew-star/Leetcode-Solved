class MinStack(object):

    def __init__(self):
        self.s1=[]
        self.min_s1=[]
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s1.append(val)
        if not self.min_s1:
            self.min_s1.append(val)
        else:
            self.min_s1.append(min(self.s1[-1],self.min_s1[-1]))


        

    def pop(self):
        """
        :rtype: None
        """
        self.min_s1.pop()
        return self.s1.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.s1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s1[-1]
        


