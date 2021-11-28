import import_ipynb
from algorithms_and_data_structures import LinkedListOnNode
from algorithms_and_data_structures import LinkedListOnNestedList
from itertools import permutations
from mock import Mock
import pytest


@pytest.mark.parametrize(
    "LinkedList",
    [
        LinkedListOnNestedList,
        LinkedListOnNode,
    ]
)
def test_LinkedList(LinkedList):

    # test insert/pop 1 object index = 0
    obj = Mock()
    linked_list = LinkedList()
    linked_list.insert(obj)
    assert linked_list.pop() is obj

    # test insert/pop 2 objects index = 0
    obj1, obj2 = Mock(), Mock()
    linked_list = LinkedList()
    linked_list.insert(obj1)
    linked_list.insert(obj2)
    assert linked_list.pop() is obj2
    assert linked_list.pop() is obj1

    # test insert/pop 2 objects index = 0
    obj1, obj2 = Mock(), Mock()
    linked_list = LinkedList()
    linked_list.insert(obj1)
    assert linked_list.pop() is obj1
    linked_list.insert(obj2)
    assert linked_list.pop() is obj2

    # test insert/pop 3 objects index = 1
    obj1, obj2, obj3 = Mock(), Mock(), Mock()
    linked_list = LinkedList()
    linked_list.insert(obj1)
    linked_list.insert(obj2)
    linked_list.insert(obj3, index=1)
    assert linked_list.pop() is obj2
    assert linked_list.pop() is obj3
    assert linked_list.pop() is obj1

    # test insert/pop 3 objects index = 1
    obj1, obj2, obj3 = Mock(), Mock(), Mock()
    linked_list = LinkedList()
    linked_list.insert(obj1)
    linked_list.insert(obj2)
    linked_list.insert(obj3)
    assert linked_list.pop(index=1) is obj2
    assert linked_list.pop() is obj3
    assert linked_list.pop() is obj1

    # test insert/pop N objects index = 0
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for obj in objs:
        linked_list.insert(obj)

    for obj in objs[::-1]:
        assert linked_list.pop() is obj

    # test insert/pop N objects index = 0
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for obj in objs:
        linked_list.insert(obj)
        assert linked_list.pop() is obj

    # test insert/pop N objects index = 10
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for obj in objs:
        linked_list.insert(obj)

    obj = Mock()
    linked_list.insert(obj, index=10)
    assert linked_list.pop() is objs[-1]
    assert linked_list.pop(9) is obj

    # test insert/pop N objects index = 10
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for obj in objs:
        linked_list.insert(obj)
    
    assert linked_list.pop(10) is objs[-11]

    # test len 1 objects
    linked_list = LinkedList()
    assert len(linked_list) == 0
    linked_list.insert(obj1)
    assert len(linked_list) == 1
    linked_list.pop()
    assert len(linked_list) == 0

    # test len 2 objects
    linked_list = LinkedList()
    obj1, obj2 = Mock(), Mock()
    assert len(linked_list) == 0
    linked_list.insert(obj1)
    assert len(linked_list) == 1
    linked_list.insert(obj2)
    assert len(linked_list) == 2
    linked_list.pop()
    assert len(linked_list) == 1
    linked_list.pop()
    assert len(linked_list) == 0

    # test len 2 objects
    linked_list = LinkedList()
    obj1, obj2 = Mock(), Mock()
    assert len(linked_list) == 0
    linked_list.insert(obj1)
    assert len(linked_list) == 1
    linked_list.pop()
    assert len(linked_list) == 0
    linked_list.insert(obj2)
    assert len(linked_list) == 1
    linked_list.pop()
    assert len(linked_list) == 0

    # test len N objects
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for i, obj in enumerate(objs):
        assert len(linked_list) == i
        linked_list.insert(obj)
        assert len(linked_list) == i + 1

    for i, obj in enumerate(objs):
        assert len(linked_list) == N - i
        linked_list.pop()
        assert len(linked_list) == N - i - 1

    # test len N objects
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for i, obj in enumerate(objs):
        assert len(linked_list) == 0
        linked_list.insert(obj)
        assert len(linked_list) == 1
        linked_list.pop()
        assert len(linked_list) == 0

    # test reverse 1 object
    obj = Mock()
    linked_list = LinkedList()
    linked_list.insert(obj)
    linked_list.reverse()
    assert linked_list.pop() is obj

    # test reverse N objects
    N = 1000
    objs = [Mock() for _ in range(N)]
    linked_list = LinkedList()

    for obj in objs:
        linked_list.insert(obj)

    linked_list.reverse()

    for obj in objs:
        assert linked_list.pop() is obj




























    # itr = range(n)
    # obj = structure()

    # assert obj.is_empty()

    # for i in itr:
    #     push(obj, i)
    #     assert not obj.is_empty()
    #     assert i == pop(obj).key
    #     assert obj.is_empty()

    # assert obj.is_empty()

    # for i in itr:
    #     push(obj, i)

    # for i in reversed(itr):
    #     assert not obj.is_empty()
    #     assert pop(obj).key == i

    # assert obj.is_empty()

    # with pytest.raises(IndexError):
    #     pop(obj)

    # for i in itr:
    #     obj.insert(i, i)
 
    # for i in itr:
    #     assert pop(obj).key == i
    
    # for i in itr:
    #     obj.insert(i)
    
    # for i, j in zip(range(n//2), range(n-1,-1, 2)):
    #     assert pop(obj, i).key == j

















# def return_sort_array(function_sort, array, *args):
#     array_for_sort = array.copy()
#     function_sort(array_for_sort, *args)
#     return array_for_sort


# def test_sorts():
#     functions_sort = (
#         algs.choice_sort,
#         algs.insert_sort,
#         algs.bubble_sort,
#         algs.merge_sort,
#         algs.quick_sort,
#         algs.heap_sort,
#     )

#     for function in functions_sort:
#         for array in permutations(range(6)):
#             assert return_sort_array(function, list(array)) == list(range(6))
#         assert return_sort_array(function, [1]) == [1]
#         assert return_sort_array(function, []) == []


# def test_count_sort():
#     for array in permutations(range(6)):
#             assert return_sort_array(algs.count_sort,
#                                      list(array),
#                                      list(range(6))) == list(range(6))
#     assert return_sort_array(algs.count_sort, [], [1, 2, 3, 4, 5]) == []
#     assert return_sort_array(algs.count_sort, [3, 4, 1],
#                              [1, 2, 3, 4, 5]) == [1, 3, 4]
#     assert return_sort_array(algs.count_sort,
#                              [5]*10 + [3]*5 + [9]*9 + [1]*3 + [5]*3,
#                              [1, 3, 5, 9]) == ([1]*3 + [3]*5 + [5]*13
#                                                + [9]*9)


# class KeyVal:

#     def __init__(self, key, val):
#         self.val = val
#         self.key = key

#     def __lt__(self, other):
#         return self.key < other.key

#     def __le__(self, other):
#         return self.key <= other.key

#     def __eq__(self, other):
#         return self.key == other.key

#     def __gt__(self, other):
#         return self.key > other.key

#     def __ge__(self, other):
#         return self.key >= other.key

# def return_sort_tuple(func, array_KeyVal):
#     return [(x.key, x.val) for x in return_sort_array(func, array_KeyVal)]


# def test_stable():
#     functions_sort = (
#         algs.insert_sort,
#         algs.bubble_sort,
#         algs.merge_sort,
#     )

#     for function in functions_sort:
#         assert return_sort_tuple(function, [
#                                             KeyVal(1, 1),
#                                             KeyVal(2, 1),
#                                             KeyVal(1, 2)
#                                            ]
#                                 ) == [(1, 1), (1, 2), (2, 1)]
#         assert return_sort_tuple(function, [
#                                             KeyVal(1, 2),
#                                             KeyVal(1, 1)
#                                            ]
#                                 ) == [(1, 2), (1, 1)]
#         assert return_sort_tuple(function, [
#                                             KeyVal(1, 1),
#                                             KeyVal(1, -8),
#                                             KeyVal(1, 2),
#                                             KeyVal(2, 1),
#                                             KeyVal(2, 3),
#                                             KeyVal(2, 2),
#                                             KeyVal(1, 1),
#                                             KeyVal(1, 3),
#                                             KeyVal(1, 2),
#                                            ]
#                                 ) == [(1, 1), (1, -8), (1, 2),
#                                       (1, 1), (1, 3), (1, 2),
#                                       (2, 1), (2, 3), (2, 2)]
#         assert return_sort_tuple(function, [
#                                             KeyVal(2, 3),
#                                             KeyVal(1, 1),
#                                             KeyVal(2, 1),
#                                             KeyVal(1, 2)
#                                            ]
#                                 ) == [(1, 1), (1, 2), (2, 3), (2,1)]


# def test_search():
#     functions_search = (
#         algs.liner_search,
#         algs.binary_search,
#     )

#     for function in functions_search:
#         assert function(1, [1, 2, 3, 4, 5]) == 0
#         assert function(5, [1, 2, 3, 4, 5]) == 4
#         assert function(0, [1, 2, 3, 4, 5]) is None
#         assert function(6, [1, 2, 3, 4, 5]) is None
#         assert function(10, [1, 2, 3, 4, 5]) is None
#         assert function(-1, [1, 2, 3, 4, 5]) is None
#         assert function(1, []) is None
#         assert function(1, [1]) == 0
#         assert function(1, [1, 2]) == 0
#         assert function(2, [1, 2]) == 1


# def test_fibonachi():
#     functions_fibonachi = (
#         algs.fibonachi_recursive,
#         algs.fibonachi_dinamic,
#     )

#     for function in functions_fibonachi:
#         assert function(1) == 1
#         assert function(2) == 1
#         assert function(3) == 2
#         assert function(4) == 3
#         assert function(5) == 5
#         assert function(6) == 8
#         assert function(7) == 13
#         assert function(8) == 21


# def sum_on_python():
#     assert algs.sum_on_python([0]) == 0
#     assert algs.sum_on_python([1, 2, 3, 4, 5]) == 15
#     assert algs.sum_on_python([0, 0, 0, 0, 0]) == 0
#     assert algs.sum_on_python([1, 1, 1, 1, 1]) == 5
#     assert algs.sum_on_python([10, 20, 30]) == 60
#     assert algs.sum_on_python([-100, 1]) == -99


# def prod():
#     assert algs.prod([0]) == 0
#     assert algs.prod([1, 2, 3, 4, 5]) == 120
#     assert algs.prod([0, 0, 0, 0, 0]) == 0
#     assert algs.prod([1, 1, 1, 1, 1]) == 1
#     assert algs.prod([10, 20, 30]) == 6000
#     assert algs.prod([-100, 1]) == -100


# def test_equal():
#     assert algs.equal([0], [0])
#     assert not algs.equal([1, 2, 3], [-1, -2, -3])
#     assert algs.equal([1, 2, 3, 4], [1, 2, 3, 4])
#     assert algs.equal('test', 'test')
#     assert not algs.equal('test false', 'test true')
#     assert not algs.equal('1test', '2test')


# def test_factorial():
#     assert algs.factorial(0) == 1
#     assert algs.factorial(1) == 1
#     assert algs.factorial(2) == 2
#     assert algs.factorial(3) == 6
#     assert algs.factorial(4) == 24
#     assert algs.factorial(5) == 120


# def test_pow():
#     for function in algs.pow_, algs.fast_pow:
#         assert function(2, 3) == 8
#         assert function(1, 0) == 1
#         assert function(5, 0) == 1
#         assert function(0, 10) == 0
#         assert function(10, 10) == 10_000_000_000
#         assert function(1, 1) == 1
#         assert function(1, 10) == 1


# import import_ipynb
# import pytest
# import data_structures as strs


# n = 102


# def standard_test(structure, push, pop, LIFO=True):
#     itr = range(n)
#     obj = structure(max_size=n)
    
#     assert obj.is_empty()

#     for i in itr:
#         push(obj, i)
#         assert not obj.is_empty()
#         assert i == pop(obj)
#         assert obj.is_empty()

#     assert obj.is_empty()

#     for i in itr:
#         push(obj, i)

#     assert obj.is_full()

#     with pytest.raises(MemoryError):
#         push(obj, n)

#     if LIFO:
#         itr = reversed(itr)

#     for i in itr:
#         assert not obj.is_empty()
#         assert pop(obj) == i

#     assert obj.is_empty()

#     with pytest.raises(IndexError):
#         pop(obj)


# def test_Stack():
#     standard_test(strs.Stack, strs.Stack.push, strs.Stack.pop)


# def test_Queue():
#     standard_test(strs.Queue, strs.Queue.enqueue, strs.Queue.dequeue,
#                   False)

# def test_Deque():
#     standard_test(strs.Deque, strs.Deque.enqueue_head, strs.Deque.dequeue_tail,
#                   False)
#     standard_test(strs.Deque, strs.Deque.enqueue_tail, strs.Deque.dequeue_head,
#                   False)
#     standard_test(strs.Deque, strs.Deque.enqueue_tail, strs.Deque.dequeue_tail)
#     standard_test(strs.Deque, strs.Deque.enqueue_head, strs.Deque.dequeue_head)





# # def test_LinkedList():
# #     linked_test(strs.LinkedList, strs.LinkedList.insert,
# #                 strs.LinkedList.pop)


# # def test_DoublyLinkedList():
# #     linked_test(strs.DoublyLinkedList, strs.DoublyLinkedList.insert,
# #                 strs.DoublyLinkedList.pop)


# def test_Heap():
#     structure = strs.Heap
#     push = strs.Heap.insert
#     pop = strs.Heap.extract_min
    
#     itr = range(n)
#     obj = structure()

#     assert obj.is_empty()

#     for i in itr:
#         push(obj, i)
#         assert not obj.is_empty()
#         assert i == pop(obj)
#         assert obj.is_empty()

#     assert obj.is_empty()

#     for i in itr:
#         push(obj, i)

#     for i in itr:
#         assert not obj.is_empty()
#         assert pop(obj) == i

#     assert obj.is_empty()


# def test_BinarySearchTree():
#     obj = strs.BinarySearchTree()

#     itr = range(n)

#     for i in itr:
#         obj.insert(i)

#     assert max(itr) == obj.tree_max().key
#     assert min(itr) == obj.tree_min().key
#     assert obj.sort() == list(itr)

#     obj = strs.BinarySearchTree()
#     for i in itr:
#         assert not obj.search(i)
#         obj.insert(i)
#         assert obj.search(i)

    
#     for i in itr:
#         assert i == obj.tree_min().key
#         obj.delete(obj.search(i))

#     for i in itr:
#         obj.insert(i)

#     for i in itr[1:]:
#         assert i == obj.next_element().key
#         obj.delete(obj.next_element())



# def test_Graph():
#     pass


# def test_HashTable():
#     pass



# import itertools


# N = 7


# def sort_test_of(func):
#     for length in range(N):
#         for permutation in itertools.permutations(range(length)):
#             array = list(permutation)
#             func(array)
#             assert array == list(range(length))


# sort_test_of(choice_sort)
# sort_test_of(insert_sort)
# sort_test_of(bubble_sort)
# sort_test_of(count_sort)
# sort_test_of(merge_sort)
# sort_test_of(quick_sort)
# sort_test_of(heap_sort)
# sort_test_of(lambda x: x.sort())



# import time
# import random
# import functools

# N = 10000
# array = list(range(N))
# random.shuffle(array)


# def timer_sort_of(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__}: {end-start:.2f}s")
#     return wrapper


# timer_sort_of(choice_sort)(array.copy())
# timer_sort_of(insert_sort)(array.copy())
# timer_sort_of(bubble_sort)(array.copy())
# timer_sort_of(count_sort)(array.copy())
# timer_sort_of(merge_sort)(array.copy())
# timer_sort_of(quick_sort)(array.copy())
# timer_sort_of(heap_sort)(array.copy())
# timer_sort_of(lambda x: x.sort())(array.copy())



# ### Stable test, order is stable
# # todo
# # class KeyVal:

# #     def __init__(self, key, val):
# #         self.val = val
# #         self.key = key

# #     def __lt__(self, other):
# #         return self.key < other.key

# #     def __le__(self, other):
# #         return self.key <= other.key

# #     def __eq__(self, other):
# #         return self.key == other.key

# #     def __gt__(self, other):
# #         return self.key > other.key

# #     def __ge__(self, other):
# #         return self.key >= other.key




# import itertools


# N = 100


# def serch_test_of(func):    
#     for length in range(N):
#         array = list(range(length))
#         for i in range(length+1):
#             if i == 0:
#                 value = array[0] - 0.5 if array else 0.5
#             else:
#                 value = array[i-1] + 0.5

#             new_array = array.copy()
#             new_array.insert(i, value)
#             assert func(value, new_array) == i



# serch_test_of(liner_search)
# serch_test_of(binary_search)
# serch_test_of(lambda x, array: array.index(x))


# import time
# import random
# import functools


# N = 100_000_000
# array = list(range(N))
# value = random.choice(array)


# def timer_search_of(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__}: {end-start:.2f}s")
#     return wrapper


# ### Stable test, search first value



# import functools


# N = 100


# def sum_test_of(func):
#     for length in range(N):
#         array = list(range(length))
#         assert func(array) == sum(array)


# def prod_test_of(func):
#     for length in range(N):
#         array = list(range(length))
#         assert func(array) == functools.reduce(lambda x, y: x*y, array, 1)


# def equal_test_of(func):
#     assert func([], []) == True

#     for length in range(1, N):
#         array = list(range(length))
#         assert func(array, array) == True

#         over_head_array = list(range(length+1))
#         assert func(array, over_head_array) == False

        
#         assert func(array, list(range(1, length+1))) == False


# sum_test_of(summ)
# prod_test_of(prod)
# equal_test_of(equal)


# def test_fibonachi():
#     functions_fibonachi = (
#         algs.fibonachi_recursive,
#         algs.fibonachi_dinamic,
#     )

#     for function in functions_fibonachi:
#         assert function(1) == 1
#         assert function(2) == 1
#         assert function(3) == 2
#         assert function(4) == 3
#         assert function(5) == 5
#         assert function(6) == 8
#         assert function(7) == 13
#         assert function(8) == 21


# def test_factorial():
#     assert algs.factorial(0) == 1
#     assert algs.factorial(1) == 1
#     assert algs.factorial(2) == 2
#     assert algs.factorial(3) == 6
#     assert algs.factorial(4) == 24
#     assert algs.factorial(5) == 120


# def test_pow():
#     for function in algs.pow_, algs.fast_pow:
#         assert function(2, 3) == 8
#         assert function(1, 0) == 1
#         assert function(5, 0) == 1
#         assert function(0, 10) == 0
#         assert function(10, 10) == 10_000_000_000
#         assert function(1, 1) == 1
#         assert function(1, 10) == 1
