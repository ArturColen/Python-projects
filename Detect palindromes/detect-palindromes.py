import math

def is_palindrome(word):
    j = len(word) - 1
    result = 0

    # Check if the word is a palindrome
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result + 1

        if i >= j:
            break

        j = j - 1

    if result == math.ceil(len(word)/2):
        return True
    else:
        return False

def is_palindrome_recursive(word):
    # Check the letters of the word (direct and reverse)
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])

# Words that were tested (if you want to verify others, add them to the array)
words = ['arara', 'racecar', 'carro', 'cama', 'level', 'osso']

# Show the user the results
for word in words:
    print(word)
    print(is_palindrome_recursive(word))
    print('\n')