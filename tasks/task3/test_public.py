import pytest

from .task import count_segments


class Case:
    def __init__(self, name: str, n: int, m: int, segments: list, queries: list, answers: tuple):
        self._name = name
        self.n = n
        self.m = m
        self.segments = segments
        self.queries = queries
        self.answers = answers

    def __str__(self) -> str:
        return 'task3_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base',
        n=3,
        m=3,
        segments=['1 3', '4 5', '6 7'],
        queries=['3 1 4 7', '2 4 5', '1 8'],
        answers=(3, 1, 0),
    ),
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task3(case: Case) -> None:
    answer = count_segments(n=case.n, m=case.m, segments=case.segments, queries=case.queries)
    assert answer == case.answers
