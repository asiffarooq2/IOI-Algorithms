# ==========================================
# CHECK IF TWO WORDS ARE ANAGRAMS
# ==========================================


# Function to count the frequency
# of each letter
def frequency(word):

    # Remove spaces and convert
    # all letters to lowercase
    word = word.replace(" ", "").lower()

    # Dictionary to store frequency
    counts = {}

    # Check every letter
    for letter in word:

        if letter in counts:

            counts[letter] += 1

        else:

            counts[letter] = 1

    return counts


# Function to check anagrams
def checkAnagrams(word1, word2):

    # Compare character frequencies
    if frequency(word1) == frequency(word2):

        return True

    else:

        return False


# Driver Code
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")


# Display result
print(
    "Are the words anagrams?",
    checkAnagrams(word1, word2)
)
