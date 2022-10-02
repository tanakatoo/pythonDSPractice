def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq1={}
    freq2={}
    listnum1 = [int(i) for i in str(num1)]
    listnum2 = [int(i) for i in str(num2)]
    for num in listnum1:
        if freq1.get(num):
            freq1[num] +=1
        else:
            freq1[num]=1
    for num in listnum2:
        if freq2.get(num):
            freq2[num] +=1
        else:
            freq2[num]=1
    if freq1 == freq2:
        return True
    return False