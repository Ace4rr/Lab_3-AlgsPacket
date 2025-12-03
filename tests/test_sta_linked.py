import pytest
from structs.stack_linked import StackLinked

def test_push_and_len():
    s=StackLinked()
    s.push(10)
    s.push(20)
    s.push(30)
    assert len(s)==3
    assert not s.is_empty()

def test_peek():
    s=StackLinked()
    s.push(5)
    s.push(7)

    assert s.peek()==7
    assert len(s)==2

def test_pop():
    s=StackLinked()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop()==3
    assert s.pop()==2
    assert len(s)==1
    assert s.peek()==1

def test_pop_empty():
    s=StackLinked()
    with pytest.raises(IndexError):
        s.pop()

def test_peek_empty():
    s=StackLinked()
    with pytest.raises(IndexError):
        s.peek()

def test_order_preserved():
    s=StackLinked()
    for i in range(5):
        s.push(i)
    assert [s.pop() for _ in range(5)]==[4,3,2,1,0]