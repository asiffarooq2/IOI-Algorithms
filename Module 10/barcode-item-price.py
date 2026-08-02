# ==========================================
# BARCODE ITEM PRICE
# ==========================================


# Function to calculate item price
# from barcode characters
def itemPrice(barcode):

    # List to store maximum digits
    # from ASCII codes
    values = []

    # Check every character in barcode
    for character in barcode:

        # Convert character to ASCII code
        ascii_code = ord(character)

        number = ascii_code

        # Find the largest digit
        # in the ASCII code
        if number // 10:

            maximum_digit = 0

            while number > 0:

                digit = number % 10

                if digit > maximum_digit:

                    maximum_digit = digit

                number = number // 10

            # Store largest digit
            values.append(maximum_digit)

        else:

            values.append(number)

    # Add all maximum digits
    return sum(values)


# Driver Code
barcode = input("Enter barcode: ")


price = itemPrice(barcode)


print("Item Price:", price)
