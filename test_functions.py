import pytest
from testfixtures import TempDirectory
from print_functions import *
from util_funcs import lock_depth_positive_check


def test_print_separation_line(capfd):

    print_separation_line('=', 2)
    out, err = capfd.readouterr()
    assert out == "\n\t==\n\n"

    print_separation_line('=', 0)
    out, err = capfd.readouterr()
    assert out == "\n\t\n\n"

    print_separation_line('=', 10)
    out, err = capfd.readouterr()
    assert out == "\n\t==========\n\n"

    print_separation_line('', 2)
    out, err = capfd.readouterr()
    assert out == "\n\t\n\n"

    print_separation_line('=', -1)
    out, err = capfd.readouterr()
    assert out == "\n\t\n\n"

    with pytest.raises(TypeError) as exception_info:
        print_separation_line(None, 2)
    assert exception_info.type is TypeError

def test_extract_msg_file_content():


# def test_lock_depth_positive_check():
#
