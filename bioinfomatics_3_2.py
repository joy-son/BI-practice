#!/usr/bin/env python

# fr = open("title.txt", "r")
# lines = fr.readlines()
# for line in lines:
#    line = line.strip()
#    break
# fr.close()
#    print("The first line is : %s" % (line))

with open("title.txt", "r") as fw:
    for line in fw:
        print("The first line is : %s" % (line))
        # print(type(line))
