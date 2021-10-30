#!/usr/bin/env python

l_seq = list()

# with open("sequence.protein.2.fasta", "w") as new:
#    with open("sequence.protein.fasta", "r") as contents:
#        lines = contents.read()
#        new.write(lines)
with open("sequence.protein.fasta", "r") as contents:
    for line in contents:
        line = line.strip()
        if line == "":
            continue
        l_seq.append(line)

with open("sequence.protein.2.fasta", "w") as new:
    new1 = "\n".join(l_seq)
    new.write("%s\n" % (new1))
