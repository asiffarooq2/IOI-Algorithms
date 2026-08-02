# ==========================================
# RABIN-KARP STRING SEARCH ALGORITHM
# ==========================================


# Number of characters in input alphabet
d = 10


# Function to search for pattern in text
def searchPattern(pattern, text, q):

    m = len(pattern)
    n = len(text)

    # Hash value of pattern
    p = 0

    # Hash value of current text window
    t = 0

    h = 1

    # Calculate h = d^(m-1) % q
    for i in range(m - 1):

        h = (h * d) % q

    # Calculate initial hash values
    # for pattern and first text window
    for i in range(m):

        p = (d * p + ord(pattern[i])) % q

        t = (d * t + ord(text[i])) % q

    # Slide the pattern over the text
    for i in range(n - m + 1):

        # If hash values match,
        # compare characters one by one
        if p == t:

            match = True

            for j in range(m):

                if text[i + j] != pattern[j]:

                    match = False
                    break

            if match:

                print(
                    "Pattern is found at position:",
                    i + 1
                )

        # Calculate hash for next window
        if i < n - m:

            t = (
                d * (t - ord(text[i]) * h)
                + ord(text[i + m])
            ) % q

            # Make hash positive
            if t < 0:

                t = t + q


# ==========================================
# DRIVER CODE
# ==========================================

text = "PROGRAMMINGPYTHON"
pattern = "PYTHON"

q = 13


print("Text:", text)
print("Pattern:", pattern)


searchPattern(
    pattern,
    text,
    q
)
