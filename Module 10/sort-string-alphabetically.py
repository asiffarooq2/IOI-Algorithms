# ==========================================
# SORT CHARACTERS OF A STRING
# ==========================================


# Function to sort a string
# in alphabetical order
def sortString(text):

    # List to store frequency
    # of 26 lowercase letters
    frequency = []

    # Store final sorted string
    answer = ""

    # Initialize frequency of
    # every letter with 0
    for i in range(26):

        frequency.append(0)

    # Count frequency of each character
    for i in range(len(text)):

        # Find position of character
        # a = 0, b = 1, c = 2, ...
        index = ord(text[i]) - ord('a')

        frequency[index] += 1

    # Build string in alphabetical order
    for i in range(26):

        if frequency[i] >= 1:

            # Add character according
            # to its frequency
            for j in range(frequency[i]):

                answer = answer + chr(
                    ord('a') + i
                )

    return answer


# ==========================================
# DRIVER CODE
# ==========================================

word = "python"

print("Original String:", word)

print("Sorted String:", sortString(word))
