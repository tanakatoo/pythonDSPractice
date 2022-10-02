def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dict_to_return = {}
    for letter in phrase:
        # if letter is already in dict, add 1 to it
        if letter in dict_to_return.keys():
            dict_to_return[letter] +=1
        else:
            dict_to_return[letter] = 1
    return dict_to_return