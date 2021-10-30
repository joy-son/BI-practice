#!/usr/bin/env python

s1 = str(
    input(
        "Enter a string : ",
    )
)

s2 = str(
    input(
        "Enter another : ",
    )
)

if len(s1) % 2 == 1 and len(s1) < len(s2):
    print(s1 + s2)

else:
    print(s2 + s1)
