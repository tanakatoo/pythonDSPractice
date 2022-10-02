def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped = []
    for letter in phrase:
        if letter.upper() == to_swap.upper():
            if letter.isupper():
                letter = letter.lower()
            elif letter.islower():
                letter = letter.upper()
        swapped.append(letter)
    
    return ''.join(swapped)