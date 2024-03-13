def is_even(number):
    """
    This function tells if a given number is odd or even
    Input - any valid integer
    odd - odd / even
    """
    if isinstance(number,int):
        if number % 2 ==0:
            return 'Even'
        else:
            return 'Odd'
    else:
        return 'Input Not Allowed'
