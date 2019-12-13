#!/usr/bin/python
licznik=0
for linia in file("lorem.txt"):
    if "bash" in linia:
        licznik=licznik + 1
print(licznik)

licznik=0
for linia in file("lorem.txt"):
    if len("linia")>100 in linia:
        licznik=licznik + 1
print(licznik)


import re
s="[0-9]"
r="6"
licznik=0
for linia in file("lorem.txt"):
    if re.search(s,linia):
        licznik=licznik + 1
print(licznik)


dopisuje tutaj jakies pierdolety
