from logger import logger
from collections import deque
class StackQueue:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        self.logger=logger

    def push(self, x: int) -> None:
        self.logger.debug(f"StackQueue.push({x})")
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2=self.q2, self.q1

    def pop(self) -> int:
        if not self.q1:
            self.logger.error("StackQueue.pop is empty")
            raise IndexError("pop from empty stack")
        v=self.q1.popleft()
        self.logger.debug(f"StackQueue.pop -> {v}")
        return v
    def peek(self) -> int:
        if not self.q1:
            self.logger.error("StackQueue.peek is empty")
            raise IndexError("peek from empty stack")
        return self.q1[0]

    def is_empty(self) -> bool:
        return not self.q1
    def __len__(self) -> int:
        return len(self.q1)
