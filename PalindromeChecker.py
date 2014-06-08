#!/bin/python3

""" @author Arun George, 2014
    Palindrome Checker
    Python 3.4
"""



# Function that runs the palindrome program
def runPalindrome (word):

    revIndex     = -1     # keep track of the index in reverse
    isPalindrome = True   # set the default value to True

    for i in range (len(word) // 2): # We only need to look at half of the string
        if word[i] != word[revIndex]:
            isPalindrome = False
            break # break from the loop
        revIndex -= 1

    if isPalindrome:
     print ("The word \"", word, "\" is indeed a palindrome!")
    else:
     print ("The word is not a palindrome!")

# end


# main function
def main():
    word = input("Enter a word to see if it is palindrome!")
    runPalindrome(word)
# end

# run main function
main()