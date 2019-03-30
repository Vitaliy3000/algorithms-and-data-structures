import import_ipynb
import pytest
import data_structures as strs


n = 102


def standard_test(structure, push, pop, LIFO=True):
    itr = range(n)
    obj = structure(max_size=n)
    
    assert obj.is_empty()

    for i in itr:
        push(obj, i)
        assert not obj.is_empty()
        assert i == pop(obj)
        assert obj.is_empty()

    assert obj.is_empty()

    for i in itr:
        push(obj, i)

    assert obj.is_full()

    with pytest.raises(MemoryError):
        push(obj, n)

    if LIFO:
        itr = reversed(itr)

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
                  False)

def test_Deque():
    standard_test(strs.Deque, strs.Deque.enqueue_head, strs.Deque.dequeue_tail,
                  False)
    standard_test(strs.Deque, strs.Deque.enqueue_tail, strs.Deque.dequeue_head,
                  False)
    standard_test(strs.Deque, strs.Deque.enqueue_tail, strs.Deque.dequeue_tail)
    standard_test(strs.Deque, strs.Deque.enqueue_head, strs.Deque.dequeue_head)


def linked_test(structure, push, pop):
    itr = range(n)
    obj = structure()

    assert obj.is_empty()

    for i in itr:
        push(obj, i)
        assert not obj.is_empty()
        assert i == pop(obj).key
        assert obj.is_empty()

    assert obj.is_empty()

    for i in itr:
        push(obj, i)

    for i in reversed(itr):
        assert not obj.is_empty()
        assert pop(obj).key == i

    assert obj.is_empty()

    with pytest.raises(IndexError):
        pop(obj)

    for i in itr:
        obj.insert(i, i)
 
    for i in itr:
        assert pop(obj).key == i
    
    for i in itr:
        obj.insert(i)
    
    for i, j in zip(range(n//2), range(n-1,-1, 2)):
        assert pop(obj, i).key == j



def test_LinkedList():
    linked_test(strs.LinkedList, strs.LinkedList.insert,
                strs.LinkedList.pop)


def test_DoublyLinkedList():
    linked_test(strs.DoublyLinkedList, strs.DoublyLinkedList.insert,
                strs.DoublyLinkedList.pop)


def test_Heap():
    structure = strs.Heap
    push = strs.Heap.insert
    pop = strs.Heap.extract_min
    
    itr = range(n)
    obj = structure()

    assert obj.is_empty()

    for i in itr:
        push(obj, i)
        assert not obj.is_empty()
        assert i == pop(obj)
        assert obj.is_empty()

    assert obj.is_empty()

    for i in itr:
        push(obj, i)

    for i in itr:
        assert not obj.is_empty()
        assert pop(obj) == i

    assert obj.is_empty()


def test_BinarySearchTree():
    obj = strs.BinarySearchTree()

    itr = range(n)

    for i in itr:
        obj.insert(i)

    assert max(itr) == obj.tree_max().key
    assert min(itr) == obj.tree_min().key
    assert obj.sort() == list(itr)

    obj = strs.BinarySearchTree()
    for i in itr:
        assert not obj.search(i)
        obj.insert(i)
        assert obj.search(i)

    
    for i in itr:
        assert i == obj.tree_min().key
        obj.delete(obj.search(i))

    for i in itr:
        obj.insert(i)

    for i in itr[1:]:
        assert i == obj.next_element().key
        obj.delete(obj.next_element())



def test_Graph():
    pass


def test_HashTable():
    pass
