""" Hackathon - Level 2 """

def longest_word(string):
    # Add your solution here. You can use additional functions if need be.
    # Don't forget to add a DocString for all your functions and comment your code.
    # Your functions should return values rather than printing the result although you can use printing for testing purposes.
    the_longest_word=""
    word=""
    for character in string:
        if len(word)>len(the_longest_word):
            the_longest_word=word
        if character.isalpha():
            word=word+character
        else:
            word=""
        
        
        
    
    #while there are characters in the string, until the character is a space. 
    return the_longest_word  #"Your Return Value"

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return lorem
    print(longest_word("lorem ipsum, dolor sit amet"))
    