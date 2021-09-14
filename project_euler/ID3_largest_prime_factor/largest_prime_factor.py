from math import sqrt


def get_largest_prime(x):

    primes = {2}
    value = 3
    number = x
    while value < sqrt(number):
        isPrime = True
        for k in primes:
            if value % k == 0:
                isPrime = False
                value += 2
        if isPrime:
            primes.add(value)
            if number % value == 0:
                # print(value)
                number /= value
    return number


if __name__ == '__main__':

    print(get_largest_prime(600851475143))
