class MyQueue(object):
    def __init__(self):
        self.ss1=[]
        self.ss2=[]
    def push(self, x):
        while self.ss1:
            self.ss2.append(self.ss1.pop())
        self.s1.append(x)
        while self.ss2:
            self.s1.append(self.ss2.pop())

    def pop(self):
        return self.ss1.pop()

    def peek(self):
        return self.ss1[-1]

    def empty(self):
        return not self.ss1

