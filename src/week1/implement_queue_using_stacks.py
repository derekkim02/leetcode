class MyQueue(object):

    def __init__(self):
        self.reversed = []
        self.ordered = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.reversed.append(x)

        

    def pop(self):
        """
        :rtype: int
        """

        self.peek()
        return self.ordered.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        if len(self.ordered) == 0:
            while len(self.reversed) != 0:
                self.ordered.append(self.reversed.pop())

        return self.ordered[-1]
        

    def empty(self):
        """
        :rtype: bool
        """

        return len(self.ordered) == 0 and len(self.reversed) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()