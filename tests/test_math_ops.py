import pytest
import utils.math_ops as mo

@pytest.mark.parametrize("input_num, exp_result",
                         [(2, True), (3, False)])
def test_is_even_number(input_num, exp_result):
    assert mo.is_even_number(input_num) == exp_result


@pytest.mark.parametrize("input_num, exp_result",
                         [(2, True), (3, True), (4, False)])
def test_is_prime_number(input_num, exp_result):
    assert mo.is_prime_number(input_num) == exp_result