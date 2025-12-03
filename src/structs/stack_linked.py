from logger import logger
class Node:
    def __init__(self, value, nxt=None):
        self.value=value
        self.next=nxt

class StackLinked:
    def __init__(self):
        self.head: Node|None=None
        self.size=0
        self.logger=logger
    def push(self, x: int) -> None:
        self.logger.debug(f"StackLinked.push({x})")
        self.head=Node(x, self.head)
        self.size += 1
    def pop(self) -> int:
        if self.head is None:
            self.logger.error("Empty stack")
            raise IndexError("pop from empty stack")
        v=self.head.value
        self.head=self.head.next
        self.size -= 1
        self.logger.debug(f"StackLinked.pop() -> {v}")
        return v

    def peek(self) -> int:
        if self.head is None:
            self.logger.error("Empty stack")
            raise IndexError("peek from empty stack")
        return self.head.value

    def is_empty(self) -> bool:
        return self.size==0
    def __len__(self):
        return self.size
