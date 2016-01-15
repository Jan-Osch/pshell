#!/usr/bin/python

import sys

sys.excepthook = lambda *args: None


def reduce_function(e, p, i):
    return e


previous = None
signature = 'def reduce_function(e, p, i):'
previous_signature = 'previous ='
try:
    exec (signature + str(sys.argv[1]))
    exec (previous_signature + str(sys.argv[2]))
    for index, element in enumerate(sys.stdin.readlines()):
        try:
            element = element.rstrip()
            previous = reduce_function(element, previous, index)
        except:
            pass
    print previous
    sys.stdout.flush()
except Exception as e:
    pass
