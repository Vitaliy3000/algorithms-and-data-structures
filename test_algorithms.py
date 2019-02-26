import import_ipynb
import algorithms as algs


def return_sort_array(function_sort, array, *args):
    array_for_sort = array.copy()
    function_sort(array_for_sort, *args)
    return array_for_sort


def test_sorts():
    functions_sort = (
        algs.choice_sort,
        algs.insert_sort,
        algs.bubble_sort,
        algs.merge_sort,
    )

    for function in functions_sort:
        assert return_sort_array(function,
                                 [5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
        assert return_sort_array(function,
                                 [5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]
        assert return_sort_array(function, [1]) == [1]
        assert return_sort_array(function, []) == []


def test_count_sort():
    assert return_sort_array(algs.count_sort, [5, 4, 3, 2, 1],
                             [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert return_sort_array(algs.count_sort, [], [1, 2, 3, 4, 5]) == []
    assert return_sort_array(algs.count_sort, [3, 4, 1],
                             [1, 2, 3, 4, 5]) == [1, 3, 4]
    assert return_sort_array(algs.count_sort,
                             [5]*10 + [3]*5 + [9]*9 + [1]*3 + [5]*3,
                             [1, 3, 5, 9]) == ([1]*3 + [3]*5 + [5]*13
                                               + [9]*9)


def test_search():
    functions_search = (
        algs.liner_search,
        algs.binary_search,
    )

    for function in functions_search:
        assert function(1, [1, 2, 3, 4, 5]) == 0
        assert function(5, [1, 2, 3, 4, 5]) == 4
        assert function(0, [1, 2, 3, 4, 5]) is None
        assert function(6, [1, 2, 3, 4, 5]) is None
        assert function(10, [1, 2, 3, 4, 5]) is None
        assert function(-1, [1, 2, 3, 4, 5]) is None
        assert function(1, []) is None
        assert function(1, [1]) == 0
        assert function(1, [1, 2]) == 0
        assert function(2, [1, 2]) == 1


def test_fibonachi():
    functions_fibonachi = (
        algs.fibonachi_recursive,
        algs.fibonachi_dinamic,
    )

    for function in functions_fibonachi:
        assert function(1) == 1
        assert function(2) == 1
        assert function(3) == 2
        assert function(4) == 3
        assert function(5) == 5
        assert function(6) == 8
        assert function(7) == 13
        assert function(8) == 21


def sum_on_python():
    assert algs.sum_on_python([0]) == 0
    assert algs.sum_on_python([1, 2, 3, 4, 5]) == 15
    assert algs.sum_on_python([0, 0, 0, 0, 0]) == 0
    assert algs.sum_on_python([1, 1, 1, 1, 1]) == 5
    assert algs.sum_on_python([10, 20, 30]) == 60
    assert algs.sum_on_python([-100, 1]) == -99


def prod():
    assert algs.prod([0]) == 0
    assert algs.prod([1, 2, 3, 4, 5]) == 120
    assert algs.prod([0, 0, 0, 0, 0]) == 0
    assert algs.prod([1, 1, 1, 1, 1]) == 1
    assert algs.prod([10, 20, 30]) == 6000
    assert algs.prod([-100, 1]) == -100


def test_equal():
    assert algs.equal([0], [0])
    assert not algs.equal([1, 2, 3], [-1, -2, -3])
    assert algs.equal([1, 2, 3, 4], [1, 2, 3, 4])
    assert algs.equal('test', 'test')
    assert not algs.equal('test false', 'test true')
    assert not algs.equal('1test', '2test')


def test_factorial():
    assert algs.factorial(0) == 1
    assert algs.factorial(1) == 1
    assert algs.factorial(2) == 2
    assert algs.factorial(3) == 6
    assert algs.factorial(4) == 24
    assert algs.factorial(5) == 120
