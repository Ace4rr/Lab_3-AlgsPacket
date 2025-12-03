from logger import logger
class QueueList:
    def __init__(self):
        self.data=[]
        self.logger=logger
    def enqueue(self, x: int) -> None:
        self.logger.debug(f"QueueList.enqueue({x})")
        self.data.append(x)
    def dequeue(self) -> int:
        if not self.data:
            self.logger.error("QueueList.dequeue is empty")
            raise IndexError("dequeue from empty queue")
        v=self.data.pop(0)
        self.logger.debug(f"QueueList.dequeue -> {v}")
        return v

    def front(self) -> int:
        if not self.data:
            self.logger.error("QueueList.front is empty")
            raise IndexError("front from empty queue")
        return self.data[0]

    def is_empty(self) -> bool:
        return len(self.data)==0
    def __len__(self):
        return len(self.data)
