import pytest

from .task import get_elements


class Case:
    def __init__(self, name: str, n: int, a: list, m: int, queries: list, answers: tuple):
        self._name = name
        self.n = n
        self.a = a
        self.m = m
        self.queries = queries
        self.answers = answers

    def __str__(self) -> str:
        return 'task2_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=5,
        a=[2, 4, 3, 1, 5],
        m=4,
        queries=['g 3', 'a 2 4 10', 'g 3', 'g 1'],
        answers=(3, 10, 2),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task2(case: Case) -> None:
    answer = get_elements(n=case.n, a=case.a, m=case.m, queries=case.queries)
    assert answer == case.answers
