from tabulate import tabulate
from helper_functions import clear_cli, print_items, print_numbered_list, check_input_int
import pytest
from unittest import mock 
import builtins

def test_clear_cli():
    pass

def test_print_items():
    test_list = [1,2,3,4]
    def results(list):
        for item in list:
            print(item)
    result = results(test_list)
    expected = print_items(test_list)

    assert result == expected

def test_print_numbered_list():
    test_list = [{1: 1},{2:2},{3:3},{4:4}]

    def results(list):
        print(tabulate(list, headers="keys", tablefmt="pretty", showindex='always'))

    result = results(test_list)
    expected = print_numbered_list(test_list)

    assert result == expected

def test_check_input_int():
    test_menu = [{1:'1'},{2:'2'},{3:'3'}]
    
    with mock.patch.object(builtins, 'input', lambda _: 6):
        with pytest.raises(ValueError):
            check_input_int(test_menu)
    
    # with mock.patch.object(builtins, 'input', lambda _: 6):
    #     with pytest.raises(ValueError):
    #         check_input_int(test_menu)
