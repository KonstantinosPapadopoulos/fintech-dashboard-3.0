from pytest import fixture

@fixture
def op():
    from fintech.Operations import Operations
    return Operations()

def test_add(op):
    assert op.add(1,2) == 3

def test_subtract(op):
    assert op.subtract(2,1) == 1

def test_increment(op):
    assert op.increment(1) == 2


def test_decrement(op):
    assert op.decrement(2) == 1