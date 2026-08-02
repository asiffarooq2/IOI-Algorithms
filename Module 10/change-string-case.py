# ==========================================
# CHANGE CASE OF LETTERS IN A STRING
# ==========================================


# Function to change lowercase letters
# to uppercase and uppercase to lowercase
def changeTheCase(text):

    result = ""

    # Check each character in the string
    for character in text:

        # Change lowercase to uppercase
        if character.islower():

            result = result + character.upper()

        # Change uppercase to lowercase
        elif character.isupper():

            result = result + character.lower()

        # Keep spaces, numbers and symbols unchanged
        else:

            result = result + character

    return result


# Driver Code
text = input("Enter String: ")


print(
    "String after changing lowercase "
    "to uppercase and vice versa:"
)

print(changeTheCase(text))