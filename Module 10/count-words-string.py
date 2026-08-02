# ==========================================
# COUNT NUMBER OF WORDS IN A STRING
# ==========================================


# Function to count the number
# of words in a string
def countWords(text):

    count = 0

    # Remove leading and trailing spaces
    text = text.strip()

    # Check each character
    for i in range(len(text)):

        # A space indicates the end
        # of a word
        if text[i] == " ":

            count += 1

    # Add 1 for the last word
    return count + 1


# Driver Code
text = input("Enter a sentence: ")


# Display number of words
print(
    "Number of words:",
    countWords(text)
)
