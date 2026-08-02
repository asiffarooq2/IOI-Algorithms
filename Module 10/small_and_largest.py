# ==========================================
# SMALLEST AND LARGEST WORD IN A SENTENCE
# ==========================================


# Function to find smallest and largest words
def smallest_largest_words(str1):

    # Variable to build each word
    word = ""

    # List to store all words
    all_words = []

    # Add extra space so the last word
    # is also captured
    str1 = str1 + " "

    # Extract words from the sentence
    for character in str1:

        # Build the current word
        if character != " ":

            word = word + character

        else:

            # Add completed word to list
            if word != "":

                all_words.append(word)

                # Reset for next word
                word = ""

    # Check if no words were entered
    if len(all_words) == 0:

        return "", ""

    # Initially assume first word is
    # both smallest and largest
    small = all_words[0]
    large = all_words[0]

    # Find smallest and largest words
    for current_word in all_words:

        # Check for smallest word
        if len(current_word) < len(small):

            small = current_word

        # Check for largest word
        if len(current_word) > len(large):

            large = current_word

    # Return both words
    return small, large


# ==========================================
# DRIVER CODE
# ==========================================

sentence = input("Enter a sentence: ")


smallest, largest = smallest_largest_words(sentence)


print("Smallest word:", smallest)

print("Largest word:", largest)
