from mypackage import myModule
def test_top_n():
    assert myModule.top_n([8,3,2,7,5,6],3) == [8,7,6], 'incorrect'
    assert myModule.top_n([1,4,10,12,9,2],2) == [12,10], 'incorrect'
    