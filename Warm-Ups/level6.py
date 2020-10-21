""" Hackathon - Level 6 """

def cipher(string, x):
    """
    Shifts characters positions in the alphabet
    :param string: the input message to be encoded
    :param x: the number of character positions to shift
    :return: the encoded message
    """
    encrypted = ""
    for character in string:
        encrypted += chr(max((ord(character) + x) % 123, 97))
    return encrypted

if __name__ == '__main__':
    # As per the example, this should return salve
    print(cipher('pxisb', 3))
