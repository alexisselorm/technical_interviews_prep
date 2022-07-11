class MinStack(object):

    def __init__(self):
        """_summary_
        """
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1][0]:
            self.minStack.append([val,1])
        elif self.minStack[-1][0] ==val:
            self.minStack[-1][1] +=1
    def pop(self):
        """
        :rtype: None
        """
        if self.minStack[-1][0]==self.stack[-1]:
            self.minStack[-1][1] -=1
        
        if self.minStack[-1][1] == 0:
            self.minStack.pop()
            
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1][0]
 