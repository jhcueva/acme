from tempfile import tempdir
import pytest
import os
from main import read_file


def test_wrong_file(capsys):
    input = "/home/baeto/Documents/technicalTest/testInput.tx"
    with pytest.raises(SystemExit) as e:
        read_file(input)
        
    out, _ = capsys.readouterr()

    assert e.type == SystemExit
    assert e.value.code == 1
    assert out == 'Oops! No such file or directory\n'
    
def test_read_file(tmpdir):
    data = "RENE=MO10:15-12:00\n ASTRID=MO10:00-12:00"
    file_path = os.path.join(tmpdir, "file.txt")
    
    with open(file_path, 'w') as file:
        file.write(data)

    assert read_file(file_path) == ['RENE=MO10:15-12:00', 'ASTRID=MO10:00-12:00']
    
    
    
    
