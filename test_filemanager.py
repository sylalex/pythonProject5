import os
import platform
import shutil


def test_platform():
    assert platform.system() == 'Windows'


def test_copy():
    dir1 = 'consol_filemanager.py'
    dir2 = 'consol_filemanager2.py'
    shutil.copy(dir1, dir2, follow_symlinks=False)
    assert dir2 in os.listdir()
    os.remove(dir2)

def test_year():
    year = '1799'
    assert year == '1799'
