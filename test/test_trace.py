# -*- coding: utf-8 -*-
import trace


def test_trace_package():
    my_str = "duongnguyen1996"
    rev_str = trace.reverse(my_str)
    assert rev_str == "6991neyugngnoud"
