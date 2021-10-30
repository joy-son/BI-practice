#!/usr/bin/env python

i = int(
    input(
        "Enter a integer : ",
    )
)
ii = int(
    input(
        "Enter another : ",
    )
)

if i > ii:  # print(i, "is greater than", ii)
    print("%d is greater than %d" % (i, ii))
elif i < ii:  # print(i, "is less than", ii)
    print("%d is less than %d" % (i, ii))
elif i == ii:  # print(i, "is equal to", ii)
    print("%d is equal to %d" % (i, ii))
