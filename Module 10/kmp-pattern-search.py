# ==========================================
# KMP PATTERN SEARCH ALGORITHM
# ==========================================


# Function to search pattern in text
def KMPpattern(pattern, text):

    M = len(pattern)
    N = len(text)

    # LPS array stores Longest
    # Prefix which is also Suffix
    lps = [0] * M

    # Index for pattern
    j = 0

    # Calculate LPS array
    LPSArray(pattern, M, lps)

    # Index for text
    i = 0

    # Search pattern in text
    while (N - i) >= (M - j):

        # Characters match
        if pattern[j] == text[i]:

            i += 1
            j += 1

        # Entire pattern found
        if j == M:

            print(
                "Found pattern at index",
                i - j
            )

            # Continue searching
            j = lps[j - 1]

        # Character mismatch
        elif i < N and pattern[j] != text[i]:

            # Use LPS value instead of
            # starting from beginning
            if j != 0:

                j = lps[j - 1]

            else:

                i += 1


# Function to create LPS array
def LPSArray(pattern, M, lps):

    # Length of previous longest
    # prefix which is also suffix
    length = 0

    # First LPS value is always 0
    lps[0] = 0

    # Start from second character
    i = 1

    while i < M:

        # Characters match
        if pattern[i] == pattern[length]:

            length += 1

            lps[i] = length

            i += 1

        # Characters do not match
        else:

            if length != 0:

                length = lps[length - 1]

            else:

                lps[i] = 0

                i += 1


# ==========================================
# DRIVER CODE
# ==========================================

text = input("Enter the text: ")

pattern = input("Enter the pattern: ")


KMPpattern(
    pattern,
    text
)
