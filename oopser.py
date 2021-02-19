
# Tests:
def addr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    return a[op[3]] == ra + rb

def addi(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    return a[op[3]] == ra + rb

def mulr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    return a[op[3]] == ra * rb

def muli(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    return a[op[3]] == ra * rb

def banr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    return a[op[3]] == ra & rb

def bani(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    return a[op[3]] == ra & rb

def borr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    return a[op[3]] == ra | rb

def bori(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    return a[op[3]] == ra | rb

def setr(op, b, a):
    ra = b[op[1]]
    return a[op[3]] == ra

def seti(op, b, a):
    ra = op[1]
    return a[op[3]] == ra

def gtir(op, b, a):
    ra = op[1]
    rb = b[op[2]]
    if ra > rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

def gtri(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    if ra > rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

def gtrr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    if ra > rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

def eqir(op, b, a):
    ra = op[1]
    rb = b[op[2]]
    if ra == rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

def eqri(op, b, a):
    ra = b[op[1]]
    rb = op[2]
    if ra == rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

def eqrr(op, b, a):
    ra = b[op[1]]
    rb = b[op[2]]
    if ra == rb:
        return a[op[3]] == 1
    else:
        return a[op[3]] == 0

ops = (addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr)

allowed = [set(ops) for i in range(16)]

for line in open("1891_samples.txt"):
    if line.startswith("Before: "):
        b = eval(line[8:])
    elif line.startswith("After: "):
        a = eval(line[8:])
        opcode = op[0]
        badops = set()
        for func in allowed[opcode]:
            if not func(op, b, a):
                badops.add(func)
        allowed[opcode] = allowed[opcode] - badops
    else:
        op = line.strip().split()
        if len(op) == 0:
            continue
        elif len(op) == 4:
            op = [int(i) for i in op]
        else:
            print("OOPS!!")

known = set()
loop = 0
while len(known) < 16 and loop < 40:
    for i in range(16):
        print(i, [f.__name__ for f in allowed[i]])
        if len(allowed[i]) == 1:
            known.update(allowed[i])
        else:
            allowed[i] = allowed[i] - known

    print("\n\n\n")
    loop += 1
