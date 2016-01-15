#!/usr/bin/python

import sys

sys.excepthook = lambda *args: None


def filter_function(e, i):
    return True


signature = 'def filter_function(e, i):'
try:
    exec (signature + str(sys.argv[1]))  # dangerous
    for index, element in enumerate(sys.stdin.readlines()):
        try:
            element = element.rstrip()
            if filter_function(element, index):
                print(element)
                sys.stdout.flush()
        except:
            pass

except Exception as e:
    pass
