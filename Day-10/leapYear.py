def is_leap_year(year):
    # Below are doc string
    """
    - on every year that is divisible by 4 with no remainder
    - except every year that is evenly divisible by 100 with no remainder 
    - unless the year is also divisible by 400 with no remainder       
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
is_leap_year(2024)
