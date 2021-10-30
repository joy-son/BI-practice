#!/usr/bin/env python

c_line = 0

with open("sequence.protein.2.fasta", "r") as fr:
    for line in fr:
        line = line.strip()
        if c_line == 1:
            break
        c_line += 1

print("The second line is : %s" % (line))
