class MyStack:
    def __init__(self):
        self.queue1=collections.deque()

    def push(self, x):
        q2=self.queue1
        q2.append(x)
        for f in range(len(q2)-1):
            q2.append(q2.popleft())
        
    def pop(self):
        return self.queue1.popleft()

    def top(self):
        return self.queue1[0]
    
    def empty(self):
        return not len(self.queue1)