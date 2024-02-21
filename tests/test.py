from mypackage1 import myModule1

def test_top_n():
    """

    makes sure the function top_n works correctly
    """

    assert myModule1.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'Incorrect'
    assert myModule1.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'Incorrect'
    assert myModule1.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'Incorrect'
