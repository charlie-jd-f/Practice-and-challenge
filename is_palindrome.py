# Code which checks if a string is a palindrome

def is_palindrome(string):

    # convert characters all into lowercase
    string = string.lower()
    
    # store characters into temp string
    temp_list = [char for char in string if char.isalpha()]

    # place characters back into string without spaces
    string = ''.join(temp_list)

    # return true if the string is the same as its reverse
    output = True if string == string[::-1] else False

    return output

print(is_palindrome("radar"))