#!/usr/bin/env python

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

# from bioinfomatics_3_6 import seq

while True:
    pos = input("Position : ",)
    if pos == "XXX":
        print("Okay, I will stop.")
        break
    elif not pos.isdigit():
        print("You should type integer.")
        print("Please try again.")
        break
    else:
        start = (int(pos)) - 1
        end = start + 3
        print("Three amino acids : ", seq[start:end])
