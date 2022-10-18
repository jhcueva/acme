import pytest

from main import employeesCombination


@pytest.mark.parametrize(
    "inputData, expectedOutput",
    [
        (
            ['ANDRES', 'ASTRID', 'RENE', 'SARA'],
            [['ANDRES', 'ASTRID'], ['ANDRES', 'RENE'], ['ANDRES', 'SARA'], ['ASTRID', 'RENE'], ['ASTRID', 'SARA'], ['RENE', 'SARA']]
        ),
        (
            ['ANDRES', 'ASTRID', 'RENE'],
            [['ANDRES', 'ASTRID'], ['ANDRES', 'RENE'], ['ASTRID', 'RENE']]
        ),
        (
            ['ASTRID', 'RENE'],
            [['ASTRID', 'RENE']]
        ),
        (
            ['ASTRID'],
            []
        ),
        (
            [],
            []
        )
    ]
)
def test_employeeCombination(inputData, expectedOutput):
    "Test possible employees combinations"
    assert employeesCombination(inputData) == expectedOutput