from logger import logger
class QueueStack:
    def __init__(self):
        self.inbox=[]
        self.outbox=[]
        self.logger=logger

    def enqueue(self, x: int) -> None:
        self.logger.debug(f"QueueStack.enqueue({x})")
        self.inbox.append(x)
    def dequeue(self) -> int:
        if not self.inbox and not self.outbox:
            self.logger.error("QueueStack.dequeue is empty")
            raise IndexError("dequeue from empty queue")
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        v=self.outbox.pop()
        self.logger.debug(f"QueueStack.dequeue -> {v}")
        return v

    def front(self) -> int:
        if not self.inbox and not self.outbox:
            self.logger.error("QueueStack.front is empty")
            raise IndexError("front from empty queue")
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]

    def is_empty(self) -> bool:
        return not (self.inbox or self.outbox)
    def __len__(self) -> int:
        return len(self.inbox) + len(self.outbox)
