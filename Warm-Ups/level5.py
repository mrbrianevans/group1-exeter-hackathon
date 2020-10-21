""" Hackathon - Level 5 """

def convert(numeral):
    # Add your solution here. You can use additional functions if need be.
    # Don't forget to add a DocString for all your functions and comment your code.
    # Your functions should return values rather than printing the result although you can use printing for testing purposes.
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(numeral):
         if i+1<len(numeral) and numeral[i:i+2] in roman:
            num+=roman[numeral[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[numeral[i]]
            i+=1
      return num #"Your Return Value"

if __name__ == '__main__':
    # Add any code to test your solution here
    # As per the example, this should return 1145
    print(convert('MMCXLV'))
    