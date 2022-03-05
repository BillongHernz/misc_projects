

def flip_bits(bit_num):

    bit_arr = ['0' if x == '1' else '1' for x in str(bit_num)]
    return "".join(map(str, bit_arr))


def add_bit(bit_num, bit_add):

    curr = -1
    len_bit = len(str(bit_num))
    bit_arr = [int(x) for x in str(bit_num)]

    while bit_arr[curr] != 0 and abs(curr) < len_bit:
        bit_arr[curr] = 0
        curr -= 1

    if abs(curr) <= len_bit and bit_arr[curr] == 0:
        bit_arr[curr] = 1
    else:
        bit_arr[curr] = 0

    return "".join(map(str, bit_arr))


def twos_complement(bit_num):

    # print(bit_num)

    bit = flip_bits(bit_num)
    # print(bit)

    bit = add_bit(bit, 1)
    # print(bit)

    print(f'The bit complement -> {bit_num} : {bit}')

    return bit


def main():

    twos_complement('000')
    twos_complement('001')
    twos_complement('010')
    twos_complement('011')
    twos_complement('100')
    twos_complement('101')
    twos_complement('110')
    twos_complement('111')


if __name__ == '__main__':
    main()

