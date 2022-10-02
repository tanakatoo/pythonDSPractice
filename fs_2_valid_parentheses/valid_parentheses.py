def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) %2 != 0:
        return False
    for i in range(0,len(parens)):
        if i %2 ==0 and parens[i] !="(":
            return False
        elif i %2 ==1 and parens[i] != ')':
            return False
        
    return True
