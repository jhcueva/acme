import os

import pytest
from main import run


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00\n ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
            "RENE-ASTRID: 3\n"
        ),
        (
            "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00\nASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00\nANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00",
            "RENE-ASTRID: 2\nRENE-ANDRES: 2\nASTRID-ANDRES: 3\n"
        ),
        (
            "",
            ""
        )
    ]
)
def test_main(data, expected, tmpdir, capsys):
    file_path = os.path.join(tmpdir, "file.txt")

    with open(file_path, 'w') as file:
        file.write(data)

    run([None, file_path])

    out, _ = capsys.readouterr()

    assert out == expected
