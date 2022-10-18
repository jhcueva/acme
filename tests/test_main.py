import os

import pytest
from main import run


@pytest.mark.parametrize(
    "inputData, expectedOutput",
    [
        (
            "RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00\n ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
            "ASTRID-RENE: 3\n"
        ),
        (
            "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\nANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
            "ANDRES-ASTRID: 3\nANDRES-RENE: 2\nASTRID-RENE: 2\n"
        ),
        (
            "RENE=MO10:00-12:00\nASTRID=TH12:00-14:00\nANDRES=SU20:00-21:00",
            "ANDRES-ASTRID: 0\nANDRES-RENE: 0\nASTRID-RENE: 0\n"
        ),
        (
            "RENE=MO10:00-12:00\nASTRID=TH12:00-14:00,SU20:00-21:00",
            "ASTRID-RENE: 0\n"
        ),
        (
            "RENE=MO10:00-12:00\nASTRID=MO09:00-10:00",
            "ASTRID-RENE: 0\n"
        ),
        (
            "ASTRID=TH12:00-14:00,SU20:00-21:00",
            ""
        ),
        (
            "",
            ""
        )
    ]
)
def test_main(inputData, expectedOutput, tmpdir, capsys):
    """Test the main program with different inputs"""
    file_path = os.path.join(tmpdir, "file.txt")

    with open(file_path, 'w') as file:
        file.write(inputData)

    run([None, file_path])

    out, _ = capsys.readouterr()

    assert out == expectedOutput
