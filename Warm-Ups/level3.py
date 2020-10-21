""" Hackathon - Level 3 """


def oddish_evenish(x):
    """
    Returns the evenness of the sum of the digits
    :param x: the number to evaluate for oddishness or evenishness
    :return: oddish if sum of digits is odd, evenish if sum of digits is even
    """
    sum_of_digits = 0
    for digit in str(x):
        sum_of_digits += int(digit)
    print(sum_of_digits)
    return "evenish" if sum_of_digits % 2 == 0 else "oddish"


if __name__ == '__main__':
    # As per the example, this should return Oddish
    print(oddish_evenish(1190))
