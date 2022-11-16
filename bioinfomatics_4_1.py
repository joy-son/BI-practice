#!/usr/bin/env python

title = ""
l_seq = list()
o_line = False
c_line = 0

with open("sequence.protein.gb", "r") as fr:
    for line in fr:
        line = line.lstrip()
        if line == "":
            continue
        if line.startswith("LOCUS"):
            title = line
        if line.startswith("ORIGIN"):
            o_line = True
        elif o_line == True:
            l_seq.append(line)
        c_line += 1

seq = "".join(l_seq)
print("title: %s" % (title))
print("seq: %s" % (seq))
