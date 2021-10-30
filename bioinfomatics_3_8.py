#!/usr/bin/env python

from sequence import seq

r_found = list()

while True:
    i_seq = input("Searching for : ",)
    if i_seq == "XXX":
        print("Okay, I will stop.")
        break
    elif i_seq.isdigit():
        print("You should type Amino acid.")
        print("Please try again.")
        break
    else:
        i = 0  # 인풋 1시작으로 하려면 1로
        for f_seq in seq:
            if f_seq == i_seq:
                r_found.append(str(i + 1))
            i += 1
        print("Found at : %s" % (",".join(r_found)))

