import pytest
from testfixtures import TempDirectory
from print_functions import *
from util_funcs import lock_depth_positive_check

"""A PyTests file used to test various functions throughout the JLock project"""


def test_print_separation_line(capfd):
    """Testing the separation line print function with different values and characters"""
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


def test_extract_msg_file_content(capfd):
    """Testing the extract file content function, testing: for successful reads and missing files"""
    # Testing for a successful read by using tempDirectory to create a file and read the contents
    with TempDirectory() as tempDir:
        temp_filename = "testFile"
        test_line = b'This is a test file for extract msg file content function.'
        tempDir.write(temp_filename, test_line)
        file_path = tempDir.path + '/' + temp_filename
        extract_msg_file_content(file_path)
    out, err = capfd.readouterr()
    assert out == " -> This is a test file for extract msg file content function.\n"
    # Testing for a missing file by passing a file that does not exist
    missing_file = 'missing_file.txt'
    with pytest.raises(FileNotFoundError) as file_error:
        extract_msg_file_content(missing_file)
    assert file_error.type is FileNotFoundError


def test_lock_depth_positive_check(capfd):
    """Test lock depth for valid inputs, testing: positive, negative and zero"""
    # Testing for success with a valid positive int
    lock_depth_positive_check(20, '20')
    out, err = capfd.readouterr()
    assert out == ""
    # Testing for an error with a negative int
    lock_depth_positive_check(-1, '-1')
    out, err = capfd.readouterr()
    assert out == "\n\tInvalid lock depth: '-1'. Must be an integer greater than 0 (zero).\n\n"
    # Testing for an error with a zero passed
    lock_depth_positive_check(0, '0')
    out, err = capfd.readouterr()
    assert out == "\n\tInvalid lock depth: '0'. Must be an integer greater than 0 (zero).\n\n"
