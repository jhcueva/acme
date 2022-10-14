import os

import pytest
from main import readFile


@pytest.mark.parametrize(
    "input",
    [
        "/home/baeto/Documents/technicalTest/testInput.tx",
        "/home/baeto/Documents/technicalTest/testIn"
    ]
)
def test_wrong_file(input, capsys):
    """Test readFile when the file path is wrong"""
    with pytest.raises(SystemExit) as e:
        readFile(input)
        
    out, _ = capsys.readouterr()

    assert e.type == SystemExit
    assert e.value.code == 1
    assert out == "Oops! No such file or directory\n"


@pytest.mark.parametrize(
    "input",
    [
        "/home/",
        "/home/baeto/"
    ]
)
def test_wrong_directory(input, capsys):
    """Test readFile when a directory is send as an argument"""
    with pytest.raises(SystemExit) as e:
        readFile(input)

    out, _ = capsys.readouterr()

    assert e.type == SystemExit
    assert e.value.code == 1

    assert out == "Oops! The path you enter is a directory, you have to enter a file path\n"


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            "RENE=MO10:15-12:00\n ASTRID=MO10:00-12:00", 
            ['RENE=MO10:15-12:00', 'ASTRID=MO10:00-12:00']
        ),
        (
            "RENE=MO10:00-12:00\n ASTRID=MO10:00-12:00\n ANDRES=MO10:00-12:00", 
            ['RENE=MO10:00-12:00', 'ASTRID=MO10:00-12:00', 'ANDRES=MO10:00-12:00']
        )
    ]
)
def test_read_file(data, expected, tmpdir):
    file_path = os.path.join(tmpdir, "file.txt")
    
    with open(file_path, 'w') as file:
        file.write(data)

    assert readFile(file_path) == expected
    
    
    
    
