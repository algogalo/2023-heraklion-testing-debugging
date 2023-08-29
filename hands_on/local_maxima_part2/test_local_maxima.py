from local_maxima import find_maxima


def test_find_maxima():
    values = [1, 3, -2, 0, 2, 1]
    expected = [1, 4]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_edges():
    values = [4, 2, 1, 3, 1, 5]
    expected = [0, 3, 5]
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_empty():
    values = []
    expected = []
    maxima = find_maxima(values)
    assert maxima == expected


def test_find_maxima_plateau_start():
    values = [2, 2, 1, 3, 1, 5]
    expected = [0, 1, 3, 5]
    maxima = find_maxima(values)
    assert maxima == expected
    #raise Exception('not yet implemented')

def test_find_maxima_plateau():
    values = [2, 2, 1, 3, 3, 1, 5, 5]
    expected = [0, 1, 3, 4, 6, 7]
    maxima = find_maxima(values)
    assert maxima == expected
    #raise Exception('not yet implemented')

def test_find_maxima_uniform():
    values = [2, 2, 2, 2]
    expected = [0, 1, 3, 4, 6, 7]
    maxima = find_maxima(values)
    assert maxima == expected
    #raise Exception('not yet implemented')

def test_find_maxima_not_a_plateau():
    raise Exception('not yet implemented')
