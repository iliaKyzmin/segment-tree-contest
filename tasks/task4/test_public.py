import pytest

from .task import count_different_numbers


class Case:
    def __init__(self, name: str, n: int, a: list, m: int, queries: list, answers: tuple):
        self._name = name
        self.n = n
        self.a = a
        self.m = m
        self.queries = queries
        self.answers = answers

    def __str__(self) -> str:
        return 'task4_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=5,
        a=[1, 2, 3, 0, 0],
        m=5,
        queries=['3 4', '2 5', '4 5', '2 2', '5 5'],
        answers=(2, 3, 1, 1, 1),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task4(case: Case) -> None:
    answer = count_different_numbers(n=case.n, a=case.a, m=case.m, queries=case.queries)
    assert answer == case.answers
