import os

with open('names.txt') as x:
    for line in x:
        line = line.strip()
        os.mkdir(str(line))
