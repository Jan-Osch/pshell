#!/usr/bin/python

import sys
from utils import *

sys.excepthook = lambda *args: None


def sort_function(e, i, l):
    return e


signature = 'def sort_function(e, i, l):'
try:
    exec (signature + str(sys.argv[1]))
    lines = sys.stdin.readlines()
    result = []
    for index, element in enumerate(lines):
        try:
            element = element.rstrip()
            result.append((sort_function(e=element, i=index, l=lines), element))
        except Exception as e :
            print e
    for row in sorted(result, key=lambda pair: pair[0]):
        print row[1]
        sys.stdout.flush()

except Exception as e:
    pass
