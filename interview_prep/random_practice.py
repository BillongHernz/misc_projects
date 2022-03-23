
def reverse_words_in_sentence(word_string):

    return " ".join(word_string.split(" ")[::-1])


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}'.format(e))


def main():

    for i in "abracadabra":
        print(i)

    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
    print(spam(3.5))

    print(reverse_words_in_sentence("Hello World"))
    print(reverse_words_in_sentence("My name is Yoda and I am a Jedi"))


if __name__ == '__main__':
    main()
