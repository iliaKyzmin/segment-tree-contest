import pytest

from .task import count_max


class Case:
    def __init__(self, name: str, n: int, a: list, m: int, queries: list, answers: tuple):
        self._name = name
        self.n = n
        self.a = a
        self.m = m
        self.queries = queries
        self.answers = answers

    def __str__(self) -> str:
        return 'task1_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=5,
        a=[1, 3, 2, 3, 3],
        m=5,
        queries=['s 1 4', 'u 3 3', 's 1 5', 'u 2 1', 's 1 5'],
        answers=(2, 4, 3),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task1(case: Case) -> None:
    answer = count_max(n=case.n, a=case.a, m=case.m, queries=case.queries)
    assert answer == case.answers
