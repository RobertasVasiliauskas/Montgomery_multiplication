def dec_to_bin(decimal):
    binary_string = bin(decimal)[2:]
    bits = [int(bit) for bit in binary_string]
    return bits


def fix_tables(items, counts):
    for i in range(len(items) - 1):
        if items[i] == 0 and items[i + 1] == 1 and counts[i + 1] == 1:
            counts[i] += 1
            items[i + 1] = -1
            counts[i + 1] = -1
        elif items[i] == 1 and counts[i] == 1 and counts[i + 1] == 1 and i != 0:
            counts[i] += 1
            items[i + 1] = -1
            counts[i + 1] = -1
        elif items[i] == 1 and counts[i] == 1 and i == 0:
            counts[i] = -1
            items[i] = -1


def remove_minus_one(arr):
    arr = list(filter(lambda a: a != -1, arr))
    return arr


def CSE(number):
    itemX = []
    counts = []

    i = 0
    while i < len(number) - 1:
        j = 1
        count = 1
        if number[i] == 1:
            while (i + j) <= len(number) - 1 and number[i + j] == 1:
                count += 1
                j += 1
            counts.append(count)
            itemX.append(1)

            i += j
        else:
            while (i + j) <= len(number) - 1 and number[i + j] == 0:
                count += 1
                j += 1
            counts.append(count)
            itemX.append(0)
            i += j

    if sum(counts) < len(number):
        itemX.append(number[len(number) - 1])
        counts.append(1)

    fix_tables(itemX, counts)
    itemX = remove_minus_one(itemX)
    counts = remove_minus_one(counts)

    result = '1 << '

    for i in range(0, len(itemX)):
        if itemX[i] == 0 and counts[i] > 1:
            result += str(counts[i])
            if i < len(itemX) - 1:
                result += ' + 1 '
            elif number[-1] == 1 and number[-2] == 0:
                result += ' + 1 '

        elif itemX[i] == 0 and counts[i] == 1:
            result += str(counts[i])
            if i < len(itemX) - 1:
                result += ' + 1 '
            elif number[-1] == 1 and number[-2] == 0:
                result += ' + 1 '

        elif itemX[i] == 1 and counts[i] > 1:
            result += str(counts[i])
            result += ' - 1 '

        elif itemX[i] == 1 and counts[i] == 1:
            result += str(counts[i])
            if i < len(itemX) - 1:
                result += ' + 1 '
            elif number[-1] == 1 and number[-2] == 0:
                result += ' + 1 '

        if i != len(itemX) - 1:
            result += '<< '

        if number[len(number) - 1] != 0 and number[len(number) - 2] == 0:
            result += ' + 1'



    return result


def convert_string_to_expression(string):
    elements = string.split()

    result = 0

    for i, element in enumerate(elements):
        if element.isdigit():
            num = int(element)
            if i == 0:
                result += num
            else:
                if elements[i - 1] == '+':
                    result += num
                elif elements[i - 1] == '-':
                    result -= num
        elif element == '<<':
            result <<= int(elements[i + 1])
        elif element == '>>':
            result >>= int(elements[i + 1])
        elif element == '+' or element == '-':
            pass

    return result


numbers = [255,19,166,23,76]
items = []

for number in numbers:
    items.append(CSE(dec_to_bin(number)))

print(items)

for item in items:
    print(convert_string_to_expression(item))

local = []
hosts = []

for item in items:
    variable = 9

    for i in range(1, item.count('<<')):
        hosts.append(convert_string_to_expression(item[0: 1 + i * variable]))
    local.append(hosts)
    hosts = []

