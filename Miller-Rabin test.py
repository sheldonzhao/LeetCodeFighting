import numpy as np
from bigfloat import *


def MillerRabinPrimalityTest(n):
    count = 0
    d = n - 1
    witness = [2, 3, 5, 7, 11]

    while d % 2 == 0:
        count += 1
        d = d / 2

    for a in witness:
        with precision(128) + RoundTowardZero:
            num1 = mod(pow(a, d), n)
        if num1 == 1:
            return True
        for i in range(0, count):
            with precision(1000) + RoundTowardZero:
                num2 = mod(pow(a, 2 ** i * d), n)
            if num2 == -1 or num2 == n - 1:
                return True
    print('n is composite, %d is witness' % a)
    return False


# print(MillerRabinPrimalityTest(18))
# print(MillerRabinPrimalityTest(1543267864443420616877677640751301))
# print(MillerRabinPrimalityTest(23456789023456789923456789923454566777888990189))
# print(MillerRabinPrimalityTest(2447952037112100847479213118326022843437705003126289))
# print(MillerRabinPrimalityTest(59545797598759584957498579859585984759457948579595794859456799501))

print(2**1543267864443420616877677)