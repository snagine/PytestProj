import algos.base_algos as algos
import pytest

@pytest.mark.parametrize("input_val, exp", [
                          [3, 6], [4, 24], [2, 2], [1, 1], [5, 120]])
def test_find_factorial_iter(input_val, exp):
    base_algos = algos.BaseAlgos()
    actual = base_algos.find_factorial_iter(input_val)
    assert exp == actual

@pytest.mark.parametrize("input_val, exp", [
                          [3, 6], [4, 24], [2, 2], [1, 1], [5, 120]])
def test_find_factorial_recur(input_val, exp):
    base_algos = algos.BaseAlgos()
    actual = base_algos.find_factorial_recur(input_val)
    assert exp == actual

@pytest.mark.parametrize("input_val, exp", [
                          [3, [0, 1, 1, 2]], [4, [0, 1, 1, 2, 3]], [0, []], [1, [0, 1]]])
def test_find_fibonacci_iter(input_val, exp):
    base_algos = algos.BaseAlgos()
    actual = base_algos.find_fibonacci_iter(input_val)
    assert exp == actual