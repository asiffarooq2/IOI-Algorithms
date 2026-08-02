# ==========================================
# LEXICOGRAPHICALLY NEXT STRING
# ==========================================


# Function to find the next word
def nextWord(text):

    # If string is empty
    if text == "":
        return "a"

    # Convert string to list
    # because strings cannot be modified directly
    characters = list(text)

    # Start from the last character
    i = len(characters) - 1

    # Move left while character is 'z'
    while i >= 0 and characters[i] == 'z':

        i -= 1

    # If all characters are 'z'
    if i == -1:

        return text + "a"

    # Move the character to the
    # next alphabet character
    characters[i] = chr(
        ord(characters[i]) + 1
    )

    # Convert all characters after it
    # to 'a'
    for j in range(i + 1, len(characters)):

        characters[j] = "a"

    # Convert list back to string
    return "".join(characters)


# Driver Code
word = input("Enter string: ")


print(
    "Next Word:",
    nextWord(word)
)
