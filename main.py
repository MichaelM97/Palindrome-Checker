#  Program Name: PalindromeTest
#  Author: Michael McCormick
#  Tests if words or sentences entered are valid palindromes


#  Gets valid user entry
while True:
    try:
        userInput = input("Please enter a word/phrase: ").upper()
    except SyntaxError:
        userInput = None
    if userInput:
        break

# Remove spaces from user input (so sentences are properly checked)
userInput = userInput.replace(' ', '')

# Checks if user entry is a palindrome
palindrome = True
for c, char in enumerate(userInput):
    if char != userInput[-c - 1]:
        print("Word/Sentence is not a palindrome.")
        palindrome = False
        break

if palindrome:
    print("Word/Sentence is a valid palindrome!!")