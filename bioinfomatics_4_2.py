#!/usr/bin/env python
from sequence2 import title
from sequence2 import seq2

lines = []
l_seq = seq2.split(" ")

for i in l_seq:
    if i.isalpha():
        lines.append(i)

seq = "".join(lines)

print("title: %s" % title)
print("seq: %s" % seq)

f = open("sequence3.txt", "w")
f.write(seq)
f.close()
