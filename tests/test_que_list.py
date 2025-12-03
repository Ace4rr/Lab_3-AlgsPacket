import pytest
from structs.queue_list import QueueList

def test_enqueue_and_len():
    q=QueueList()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert len(q)==3
    assert not q.is_empty()

def test_front():
    q=QueueList()
    q.enqueue(5)
    q.enqueue(7)
    assert q.front()==5
    assert len(q)==2

def test_dequeue():
    q=QueueList()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.dequeue()==1
    assert q.dequeue()==2
    assert len(q)==1
    assert q.front()==3

def test_dequeue_empty():
    q=QueueList()
    with pytest.raises(IndexError):
        q.dequeue()

def test_front_empty():
    q=QueueList()
    with pytest.raises(IndexError):
        q.front()

def test_order_preserved():
    q=QueueList()
    for i in range(5):
        q.enqueue(i)
    assert [q.dequeue() for _ in range(5)]==[0,1,2,3,4]
