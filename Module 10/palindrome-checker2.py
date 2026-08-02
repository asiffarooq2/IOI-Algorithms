# ==========================================
# CHECK IF A STRING IS A PALINDROME
# ==========================================


# Function to reverse a string
def reverse(text):

    return text[::-1]


# Function to check whether
# the string is a palindrome
def checkPalindrome(text):

    # Convert string to lowercase
    # to ignore case differences
    text = text.lower()

    # Reverse the string
    reversed_text = reverse(text)

    # Compare original and reversed string
    if text == reversed_text:

        return True

    else:

        return False


# Driver Code
text = input("Enter String: ")


# Check and display result
print(
    "Is Palindrome:",
    checkPalindrome(text)
)
