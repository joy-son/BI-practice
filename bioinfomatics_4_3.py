#!/usr/bin/env python
f = "sequence3.txt"
with open(f, "r") as fr:
    seq = fr.read()
num = int(input("Sample line length : "))
output = [seq[i : i + num] for i in range(0, len(seq), num)]
result = "\n".join(output)
print(result)

