import pytest

from .task import find_triplets


class Case:
    def __init__(self, name: str, n: int, a: list, answer: list):
        self._name = name
        self.n = n
        self.a = a
        self.answer = answer

    def __str__(self) -> str:
        return 'task6_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=4,
        a=[5, 2, 6, 1],
        answer=[2, 1, 1, 0],
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task6(case: Case) -> None:
    answer = find_triplets(n=case.n, a=case.a)
    assert answer == case.answer
