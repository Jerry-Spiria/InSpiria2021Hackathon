def addr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra + rb

def addi(op, r):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra + rb

def mulr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra * rb

def muli(op, r):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra * rb

def banr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra & rb

def bani(op, r):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra & rb

def borr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra | rb

def bori(op, r):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra | rb

def setr(op, r):
    ra = r[op[1]]
    r[op[3]] = ra

def seti(op, r):
    ra = op[1]
    r[op[3]] = ra

def gtir(op, r):
    ra = op[1]
    rb = r[op[2]]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

def gtri(op, r):
    ra = r[op[1]]
    rb = op[2]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

def gtrr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

def eqir(op, r):
    ra = op[1]
    rb = r[op[2]]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

def eqri(op, r):
    ra = r[op[1]]
    rb = op[2]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

def eqrr(op, r):
    ra = r[op[1]]
    rb = r[op[2]]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0

ops = [banr,addr,eqri,setr,gtrr,bori,gtir,seti,borr,bani,eqir,eqrr,gtri,addi,muli,mulr]
r = [0, 0, 0, 0, 0, 0, 0, 0]


for line in open("9918_test_prog.txt"):
    op = [int(i) for i in line.strip().split()]
    ops[op[0]](op, r)
    print(r)