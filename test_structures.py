import import_ipynb
import pytest
import data_structures as strs


n = 101


def standard_test(structure, push, pop, typ='LIFO'):
    obj = structure(max_size=n)
    assert obj.is_empty()

    for i in range(n):
        push(obj, i)
        assert not obj.is_empty()
        assert i == pop(obj)
        assert obj.is_empty()

    assert obj.is_empty()

    for i in range(n):
        push(obj, i)

    assert obj.is_full()

    with pytest.raises(MemoryError):
        push(obj, n)

    if typ == 'LIFO':
        itr = range(n-1, -1, -1)
    elif typ == 'FIFO':
        itr = range(n)

    for i in itr:
        assert not obj.is_empty()
        assert pop(obj) == i

    assert obj.is_empty()

    with pytest.raises(IndexError):
        pop(obj)


def test_Stack():
    standard_test(strs.Stack, strs.Stack.push, strs.Stack.pop)


def test_Queue():
    standard_test(strs.Queue, strs.Queue.enqueue, strs.Queue.dequeue,
                  typ='FIFO')


def test_LinkedList():
    standard_test(strs.LinkedList, strs.LinkedList.insert, strs.LinkedList.pop)


def test_DoublyLinkedList():
    standard_test(strs.DoublyLinkedList, strs.DoublyLinkedList.insert,
                  strs.DoublyLinkedList.pop)


