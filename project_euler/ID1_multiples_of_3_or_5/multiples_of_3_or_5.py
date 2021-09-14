
def add_all_multiples_of_n(multiple, x):

    result = 0
    index = 1
    while index*multiple < x:
        result += index*multiple
        index += 1
    return result


def multiples_of_n(multiple, x, multiple_set):

    index = 1
    while index*multiple < x:
        multiple_set.add(index*multiple)
        index += 1


def add_set(multiple_set):

    result = 0
    for item in multiple_set:
        result += item

    return result


if __name__ == '__main__':

    limit = 10
    m_set = set()
    multiples_of_n(3, limit, m_set)
    multiples_of_n(5, limit, m_set)
    print(add_set(m_set))
    print(add_all_multiples_of_n(3, limit) + add_all_multiples_of_n(5, limit))

    print('------------')

    limit = 1000
    m_set = set()
    multiples_of_n(3, limit, m_set)
    multiples_of_n(5, limit, m_set)
    print(add_set(m_set))
    print(add_all_multiples_of_n(3, limit) + add_all_multiples_of_n(5, limit))

