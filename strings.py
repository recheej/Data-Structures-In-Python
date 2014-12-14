__author__ = 'recheejozil'


def is_unique(string):

    characters = list(enumerate(string))

    char_dictionary = dict()

    for index, char in characters:

        if char in char_dictionary:
            return False
        else:
            char_dictionary[char] = 0

    return True


def swap(string, index, other_index):

    temp = string[index]

    string[index] = string[other_index]
    string[other_index] = temp


def reverse(string):

    characters = list(enumerate(string))

    for index, char in characters:

        other_index = (len(string) - index) - 1

        swap(string, index, other_index)

        if other_index == index + 1:
            return


def is_anagram(string_one, string_two):

    if len(string_one) != len(string_two):
        return False

    char_dict = dict()

    for char in string_one:

        if char.isspace():
            continue

        if char in char_dict:

            char_dict[char] += 1

        else:

            char_dict[char] = 1

    for char in string_two:

        if char.isspace():
            continue

        if char not in char_dict:
            return False

        else:

            if char_dict[char] == 0:

                return False

            else:

                char_dict[char] -= 1

    return True