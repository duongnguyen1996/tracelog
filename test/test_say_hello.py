# -*- coding: utf-8 -*-
import trace


def test_say_hello():
    try:
        trace.main.say_hello()
        assert True
    except Exception as e:
        print(e)
        assert False
