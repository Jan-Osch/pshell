#!/usr/bin/python

import sys

sys.excepthook = lambda *args: None


def map_function(e, i):
    return e


signature = 'def map_function(e, i):'
try:
    exec (signature + str(sys.argv[1]))
    for index, element in enumerate(sys.stdin.readlines()):
        try:
            element = element.rstrip()
            print(map_function(element, index))
            sys.stdout.flush()
        except:
            pass

except Exception as e:
    pass
