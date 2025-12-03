from logger import logger
class StackList:
    def __init__(self):
        self.data=[]
        self.logger=logger
    def push(self, x: int) -> None:
        self.logger.debug(f"StackList.push({x})")
        self.data.append(x)
    def pop(self) -> int:
        if not self.data:
            self.logger.error("StackList.pop is empty stack")
            raise IndexError("pop from empty stack")
        v=self.data.pop()
        self.logger.debug(f"StackList.pop() -> {v}")
        return v
    def peek(self) -> int:
        if not self.data:
            self.logger.error("StackList.peek is empty stack")
            raise IndexError("peek from empty stack")
        return self.data[-1]
    
    def is_empty(self) -> bool:
        return len(self.data) == 0
    def __len__(self) -> int:
        return len(self.data)
