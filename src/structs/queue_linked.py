from logger import logger
class Node:#узел связного списка?
    def __init__(self, value, nxt=None):
        self.value=value
        self.next=nxt#след элемент

class QueueLinked:
    def __init__(self):
        self.head:Node|None=None#первый эл 
        self.tail:Node|None=None#последний
        self.size=0#колво
        self.logger=logger
    def enqueue(self, x: int) -> None:#добавляет эл в конец
        self.logger.debug(f"QueueLinked.enqueue({x})")
        node=Node(x)
        if self.tail:
            self.tail.next=node
        else:
            self.head=node
        self.tail=node
        self.size+=1
    def dequeue(self) -> int:#удаляет эл сначала
        if self.head is None:
            self.logger.error("QueueLinked.dequeue is empty")
            raise IndexError("dequeue from empty queue")
        v=self.head.value
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        self.size -= 1
        self.logger.debug(f"QueueLinked.dequeue -> {v}")
        return v
    def front(self) -> int:#возвращает первый элемент
        if self.head is None:
            self.logger.error("QueueLinked.front is empty")
            raise IndexError("front from empty queue")
        return self.head.value

    def is_empty(self) -> bool:#проверяет на пустоту типа
        return self.size == 0
    def __len__(self):#длину мерит
        return self.size
