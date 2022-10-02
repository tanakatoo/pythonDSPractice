def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase_list = phrase.split(' ')
    phrase_list = [word.capitalize() for word in phrase_list]
    return ' '.join(phrase_list) 