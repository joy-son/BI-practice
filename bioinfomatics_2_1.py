#!/usr/bin/env python

gugu = input(
    "Which times table : ",
)

if not gugu.isdigit():
    print("You should type integer.")
    print("Please try again.")
elif not int(gugu) < 10:
    print("What?")
else:
    # for dan in range(int(gugu), int(gugu) * 10, int(gugu)):
    for dan in range(1, 10):
        print("%d * %d = %d" % (int(gugu), dan, int(gugu) * dan))
