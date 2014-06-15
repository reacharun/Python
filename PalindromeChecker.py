#!/bin/python3

""" @author Arun George, 2014
    Palindrome Checker
    Python 3.4
"""



# Function that runs the palindrome program
def run_palindrome(word):

    rev_index     = -1     # keep track of the index in reverse
    is_palindrome = True   # set the default value to True

    for i in range(len(word) // 2): # We only need to look at half of the string
        if word[i] != word[rev_index]:
            is_palindrome = False
            break # break from the loop
        rev_index -= 1

    if is_palindrome:
     print("The word \"", word, "\" is indeed a palindrome!")
    else:
     print("The word is not a palindrome!")

# end


# main function
def main():
    word = input("Enter a word to see if it is palindrome!")
    run_palindrome(word)
# end

# call the main function
main()
