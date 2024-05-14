from CSE import CSE, dec_to_bin, convert_string_to_expression

p = 8

Ic1 = 0xFF13A6174C
Ic2 = 0x284CA617FFFF

print(hex(Ic1))
print(hex(Ic2))

print("Współczynniki: ")
def coeff(p, num):
    mask = (1 << p) - 1
    coefficients = list()

    for idx in range(0, (len(hex(num)) - 2) // 2):
        temp = (num & (mask << idx * p)) >> idx * p
        coefficients.append(temp)

    coefficients.reverse()
    return coefficients

coefficients_1 = coeff(p, Ic1)
print(coefficients_1)
coefficients_2 = coeff(p, Ic2)
print(coefficients_2)

print("Maski bitowe: ")
def ones_shift(t: int):
    # print(bin(t).replace('0b', ''))
    mask = list(reversed([idx for idx, bit in enumerate(reversed(bin(t).replace('0b', ''))) if bit == '1']))
    print(mask)

    pass

def zeros_shift(t: int):
    # print(bin(t).replace('0b', ''))
    mask = list(reversed([idx for idx, bit in enumerate(reversed(bin(t).replace('0b', ''))) if bit == '0']))
    print(mask)

    pass


ones_shift(71)

print("Obliczanie naf: ")
def naf(E: int):
    i = 0
    Z = list()
    while E > 0:
        if E % 2 == 1:
            Z.append(2 - (E % 4))
            E -= Z[i]
        else:
            Z.append(0)
        E /= 2
        i += 1
    return list(reversed(Z))


print(naf(79))
print(bin(79))
# ones_shift(79)

print("Obliczanie final value: ")

final_val = 0
for idx, value in enumerate(reversed(naf(79))):
    print(f"{(2**idx)*value} ", end="")
    final_val += (2**idx)*value

# print()
print(final_val)

# print(0b1001111)


# CSE

# for coefficient in coefficients_1:
#     print(f"Coeff: {coefficient}")
#     print(CSE(dec_to_bin(coefficient)))

for coefficient in coefficients_2:
    print(f"Coeff: {coefficient}")
    print(convert_string_to_expression(CSE(dec_to_bin(coefficient))))



