#!/usr/bin/python

from utils import *
import sys

sys.excepthook = lambda *args: None


def map_function(e, i, l):
    return e


signature = 'def map_function(e, i, l):'
try:
    exec (signature + str(sys.argv[1]))
    lines = sys.stdin.readlines()
    for index, element in enumerate(lines):
        try:
            element = element.rstrip()
            print(map_function(e=element, i=index, l=lines))
            sys.stdout.flush()
        except:
            pass

except Exception as e:
    pass
