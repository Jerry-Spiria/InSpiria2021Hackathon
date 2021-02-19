ordered = ["6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH", "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS", "JS", "QS", "KS"]
value   = ["8S", "6H", "QS", "JH", "7S", "QH", "2S", "5S", "JS", "AS", "TS", "KS", "TH", "6S", "9S", "3S", "8H", "KH", "9H", "7H", "4S"]

import math
f = 21
tot = 0
for v in value:
    pos = ordered.index(v)
    ordered.remove(v)
    if pos:
        print(pos, "*", "math.factorial(", f, ") + "),
    f -= 1
    tot += pos * math.factorial(f)

print("\nThe number is:", tot)
print("F is ",f)


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

a = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in numberToBase(tot, 27):
    print(a[i])