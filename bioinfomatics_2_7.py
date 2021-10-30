#!/usr/bin/env python

codon_dic = {}

while True:
    d_codon = codon_dic
    i_codon = input("Enter a three-base codon to build : ",).upper()
    if i_codon == "XXX":
        print("Okay, I will switch.")
        break
    aa = input("Enter amino acid : ").upper()
    d_codon[i_codon] = aa

while True:
    i_codon = input("Enter a three-base codon to search : ",).upper()
    if i_codon == "XXX":
        print("Okay, I will stop.")
        break
    if i_codon in d_codon:
        aa = d_codon[i_codon]
        print("Amino acid for %s : %s" % (i_codon, aa))
    else:
        print("%s codon does not exist." % (i_codon))
