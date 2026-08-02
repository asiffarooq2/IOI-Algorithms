# ==========================================
# CITY LOCATION SEARCH
# ==========================================

# List of travel locations
travel_cities = [
    "Paris",
    "Dubai",
    "Singapore",
    "Tokyo",
    "Dubai",
    "Sydney",
    "Rome",
    "Dubai"
]

# City to search for
target_city = "Dubai"


# Linear Search Algorithm
def linear_search(search_list, target_value):

    matches = []

    # Check every element in the list
    for index in range(len(search_list)):

        if search_list[index] == target_value:

            # Store index where city is found
            matches.append(index)

    # If city was not found
    if not matches:

        raise ValueError(
            "{} is not in the list".format(
                target_value
            )
        )

    # Return all matching indexes
    else:

        return matches


# Function call
city_positions = linear_search(
    travel_cities,
    target_city
)


# Display result
print(
    "{} is present at the following indexes: {}".format(
        target_city,
        city_positions
    )
)
