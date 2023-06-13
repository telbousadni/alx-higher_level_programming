#!/usr/bin/python3


def multiple_returns(sentence):
    st_tuple = ()
    if len(sentence) == 0:
        st_tuple = 0, "None"
    else:
        st_tuple = len(sentence), sentence[0]
    return st_tuple
