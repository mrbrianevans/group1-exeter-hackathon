""" Hackathon - Level 4 """

def double_swap(string, a, b):
    # Add your solution here. You can use additional functions if need be.
    # Don't forget to add a DocString for all your functions and comment your code.
    # Your functions should return values rather than printing the result although you can use printing for testing purposes.
    new_string=""
    for character in string:
        if character==a:
            new_string=new_string+b
        elif character==b:
            new_string=new_string+a
        else:
            new_string=new_string+character
    return new_string #"Your Return Value"

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return ienv, ivdv, ivcv
    print(double_swap('veni, vidi, vici', 'v', 'i'))
    