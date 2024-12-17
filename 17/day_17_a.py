import sys
import re
import itertools

sys.setrecursionlimit(10**6)

A, B, C = 0, 1, 2

# The adv instruction (opcode 0) performs division. The numerator is the value
# in the A register. The denominator is found by raising 2 to the power of the
# instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2);
# an operand of 5 would divide A by 2^B.) The result of the division operation
# is truncated to an integer and then written to the A register.
ADV = 0

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and
# the instruction's literal operand, then stores the result in register B.
BXL = 1

# The bst instruction (opcode 2) calculates the value of its combo operand
# modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to
# the B register.
BST = 2

# The jnz instruction (opcode 3) does nothing if the A register is 0. However,
# if the A register is not zero, it jumps by setting the instruction pointer to
# the value of its literal operand; if this instruction jumps, the instruction
# pointer is not increased by 2 after this instruction.
JNZ = 3

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and
# register C, then stores the result in register B. (For legacy reasons, this
# instruction reads an operand but ignores it.)
BXC = 4

# The out instruction (opcode 5) calculates the value of its combo operand
# modulo 8, then outputs that value. (If a program outputs multiple values, they
# are separated by commas.)
OUT = 5

# The bdv instruction (opcode 6) works exactly like the adv instruction except
# that the result is stored in the B register. (The numerator is still read from
# the A register.)
BDV = 6

# The cdv instruction (opcode 7) works exactly like the adv instruction except
# that the result is stored in the C register. (The numerator is still read from
# the A register.)
CDV = 7

DEBUG = False

def main(file):
    reg, ins = read_data(file)
    ptr = 0
    output = []
    while ptr < len(ins):
        i, opr = ins[ptr], ins[ptr+1]
        if DEBUG:
            input()
            print()
            print("ins, operand", i, opr)
            print("combo       ", combo(reg, opr))
            print("register0   ", reg)
        if i == ADV:
            reg[A] = div(reg, opr)
        elif i == BXL:
            v = reg[B] ^ opr
            if DEBUG:
                print("reg[B] ^ opr", v)
            reg[B] = v
        elif i == BST:
            # operand only
            v = combo(reg, opr) % 8
            if DEBUG:
                print("combo(reg, opr) % 8", v)
            reg[B] = v
        elif i == JNZ:
            if reg[A] != 0:
                if DEBUG:
                    print("jump to", opr)
                ptr = opr
                continue
            if DEBUG:
                print("no jump")
        elif i == BXC:
            # no operand
            v = reg[B] ^ reg[C]
            if DEBUG:
                print("reg[B] ^ reg[C]", v)
            reg[B] = v
        elif i == OUT:
            # operand only
            v = combo(reg, opr) % 8
            if DEBUG:
                print("out: combo(reg, opr) % 8", v)
            output.append(v)
        elif i == BDV:
            reg[B] = div(reg, opr)
        elif i == CDV:
            reg[C] = div(reg, opr)
        else:
            assert False
        ptr += 2
        if DEBUG:
            print("register1   ", reg)
    print(",".join([str(x) for x in output]))

def div(reg, opr):
    num = reg[A]
    com = combo(reg, opr)
    den = 2**com
    v = int(num/den)
    if DEBUG:
        print("int(reg[A]/2**combo(reg,opr))", num, den, v)
    return v


def combo(reg, o):
    if o < 4:
        return o
    if o == 4:
        return reg[A]
    if o == 5:
        return reg[B]
    if o == 6:
        return reg[C]
    assert False

def read_data(file):
    with open(file) as f:
        tmap = f.read().split("\n\n")
    r = [int(x.split()[-1]) for x in [y for y in tmap[0].splitlines()]]
    i = [int(x) for x in tmap[1].split()[1].split(",")]
    return r, i



if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('input')
