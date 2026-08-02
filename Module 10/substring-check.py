# ==========================================
# CHECK IF A STRING IS A SUBSTRING
# ==========================================


# Function to check if s1
# is a substring of s2
def isSubstring(s1, s2):

    # Check if s1 exists inside s2
    if s1 in s2:

        # Return starting index
        return s2.index(s1)

    # Return -1 if not found
    return -1


# ==========================================
# DRIVER CODE
# ==========================================

if __name__ == "__main__":

    s1 = "Python"

    s2 = "I am learning Python programming"

    # Function call
    result = isSubstring(s1, s2)

    # Display result
    if result == -1:

        print("Not present")

    else:

        print(
            "Present at index",
            result
        )
