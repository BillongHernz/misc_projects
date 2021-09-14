
def add_fib_seq_to_limit(limit):

    a = 1
    b = 2
    result = 0

    while b < limit:

        if b % 2 == 0:
            result += b
        curr = b
        b = a + b
        a = curr

    return result


if __name__ == '__main__':

    print(add_fib_seq_to_limit(10))
    print(add_fib_seq_to_limit(40))
    print(add_fib_seq_to_limit(4000000))
