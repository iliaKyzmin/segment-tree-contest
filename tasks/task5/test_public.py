import pytest

from .task import find_triplets


class Case:
    def __init__(self, name: str, n: int, a: list, answer: int):
        self._name = name
        self.n = n
        self.a = a
        self.answer = answer

    def __str__(self) -> str:
        return 'task5_test_{}'.format(self._name)


TEST_CASES = [
    Case(
        name='base1',
        n=3,
        a=[3, 2, 1],
        answer=1,
    ),
    Case(
        name='base2',
        n=3,
        a=[2, 3, 1],
        answer=0,
    ),
    Case(
        name='base3',
        n=4,
        a=[10, 8, 3, 1],
        answer=4,
    )
]


@pytest.mark.parametrize('case', TEST_CASES, ids=str)
def test_task5(case: Case) -> None:
    answer = find_triplets(n=case.n, a=case.a)
    assert answer == case.answer
