# Tests for HW2
# Priority Points System

import os.path
import sys
from HW2 import main
from tud_tests import *

def test_HW2():

    try:
        exists = os.path.exists("HW2.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(["o","n",3.8])
    main()
    output = get_display_output()

    assert output == [
        "Priority Point System\n",
        "Freshman (F), Sophomore (O), Junior (J), Senior (S): ",
        "Had tickets last year? Yes (Y) or No (N)? ",
        "Please enter your GPA as a value between 0 and 4: ",
        "Your available points are 160"
        ]

    # Test 2
    set_keyboard_input(["J","Y",2.7])
    main()
    output = get_display_output()

    assert output == [
        "Priority Point System\n",
        "Freshman (F), Sophomore (O), Junior (J), Senior (S): ",
        "Had tickets last year? Yes (Y) or No (N)? ",
        "Please enter your GPA as a value between 0 and 4: ",
        "Your available points are 150"
        ]

    # Test 3
    set_keyboard_input(["s","n",1.9])
    main()
    output = get_display_output()

    assert output == [
        "Priority Point System\n",
        "Freshman (F), Sophomore (O), Junior (J), Senior (S): ",
        "Had tickets last year? Yes (Y) or No (N)? ",
        "Please enter your GPA as a value between 0 and 4: ",
        "Your available points are 135"
        ]

    # Test 4
    set_keyboard_input(["S","Y",3.1])
    main()
    output = get_display_output()

    assert output == [
        "Priority Point System\n",
        "Freshman (F), Sophomore (O), Junior (J), Senior (S): ",
        "Had tickets last year? Yes (Y) or No (N)? ",
        "Please enter your GPA as a value between 0 and 4: ",
        "Your available points are 195"
        ]