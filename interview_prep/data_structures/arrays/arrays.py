
def main():

    example = [0,2,43,1,45,3,1,3,5,2]
    print('Accesing idx 5 = ' + str(example[5-1]))
    print('Subarray from start of size 7 = ' + str(example[:7]))
    print('Subarray from size 7 ending at end = ' + str(example[-7:]))
    print('Subarray from 3 until before third last char = ' + str(example[2:-3]))

    # insert value at idx with format of (idx, value)
    example.insert(3, 999)
    print(example)

    # append value at the end
    example.append(90)

    # pop last value or nth value
    print(example.pop())
    print(example.pop(0))

    # search idx for first val found
    val = 999
    start = 0
    stop = 10
    print(example.index(val, start, stop))

    # remove val
    example.remove(val)

    return


if __name__ == '__main__':
    main()
