#!/usr/bin/env python

title = ""
l_seq = list()

with open("sequence.protein.2.fasta", "r") as fr:
    for line in fr:
        line = line.strip()
        if line == "":
            continue
        if line[0] != ">":
            l_seq.append(line)
        else:
            title = line

seq = "".join(l_seq)
print("title: %s" % (title))
print("seq: %s" % (seq))
