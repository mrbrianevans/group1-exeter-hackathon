""" Hackathon - Level 1 """


def min_max_product(list):
    """
    Mulitplies the min value and the max value
    :param list: the input list
    :return: the min times max values
    """
    return max(list)*min(list)


if name == 'main':
    # As per the example, this should return 200
    print(min_max_product([2, 100, 24, 15, 4, 9, 61]))
