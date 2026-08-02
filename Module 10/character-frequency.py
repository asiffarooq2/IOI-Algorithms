# ==========================================
# CHARACTER FREQUENCY IN A STRING
# ==========================================


# Function to count the frequency
# of each character in a string
def frequency(text):

    # Convert string to lowercase
    # to ignore case
    text = text.lower()

    # Dictionary to store frequency
    characters = {}

    # Traverse through the string
    for i in range(len(text)):

        # Check if character already
        # exists in dictionary
        if text[i] in characters.keys():

            characters[text[i]] += 1

        else:

            characters[text[i]] = 1

    return characters


# Driver Code
text = input("Enter String: ")


# Display character frequencies
print("Character Frequencies:")
print(frequency(text))
