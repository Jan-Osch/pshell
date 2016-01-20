import re

def col(line, number=0):
    return re.split('\ *', line)[number]
