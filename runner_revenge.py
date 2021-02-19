def addr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra + rb
    return ip+1

def addi(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra + rb
    return ip+1

def mulr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra * rb
    return ip+1

def muli(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra * rb
    return ip+1

def banr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra & rb
    return ip+1

def bani(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra & rb
    return ip+1

def borr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    r[op[3]] = ra | rb
    return ip+1

def bori(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    r[op[3]] = ra | rb
    return ip+1

def setr(op, r, ip):
    ra = r[op[1]]
    r[op[3]] = ra
    return ip+1

def seti(op, r, ip):
    ra = op[1]
    r[op[3]] = ra
    return ip+1

def gtir(op, r, ip):
    ra = op[1]
    rb = r[op[2]]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def gtri(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def gtrr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    if ra > rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def eqir(op, r, ip):
    ra = op[1]
    rb = r[op[2]]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def eqri(op, r, ip):
    ra = r[op[1]]
    rb = op[2]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def eqrr(op, r, ip):
    ra = r[op[1]]
    rb = r[op[2]]
    if ra == rb:
        r[op[3]] = 1
    else:
        r[op[3]] = 0
    return ip+1

def JMPZ(op, r, ip):
    ra = r[op[1]]
    if ra == 0:
        return op[2]+1
    return ip+1

def JMPNZ(op, r, ip):
    ra = r[op[1]]
    if ra != 0:
        return op[2]+1
    return ip+1

def RDR(op, r, ip):
    return ip+1

def WRR(op, r, ip):
    return ip+1


ops = [banr,addr,eqri,setr,gtrr,bori,gtir,seti,borr,bani,eqir,eqrr,gtri,addi,muli,mulr,JMPZ,JMPNZ,RDR,WRR]
r = [0, 0, 0, 0, 0, 0, 0, 0]
ip = 0

stream1 = []
with open("190831_encrypted.txt", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        stream1.append(ord(byte))
        byte = f.read(1)

stream2 = []
with open("381371_key.txt", "rb") as f:
    byte = f.read(1)
    while byte != b"":
        # Do stuff with byte.
        stream2.append(ord(byte))
        byte = f.read(1)

print(stream1, stream2)

"""
while True:
    op = prog[ip]

    ip += 1 # ALWAYS!!!

"""