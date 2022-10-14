# -*- coding: utf-8 -*-
import blank


def test_blank_package():
    my_str = "duongnguyen1996"
    rev_str = blank.reverse(my_str)
    assert rev_str == "6991neyugngnoud"
