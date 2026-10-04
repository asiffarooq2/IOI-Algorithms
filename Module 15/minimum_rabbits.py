# Python program to find the minimum number
# of rabbits in the forest


def minimum_rabbits(rabbit_answers, total_rabbits):

    # Store the frequency of each answer
    answer_frequency = {}

    # Count how many rabbits gave each answer
    for index in range(total_rabbits):

        answer = rabbit_answers[index]

        if answer in answer_frequency:
            answer_frequency[answer] += 1
        else:
            answer_frequency[answer] = 1

    # Store the minimum number of rabbits
    minimum_count = 0

    # Process each unique answer
    for rabbits_seen, frequency in answer_frequency.items():

        # Number of rabbits in one possible group
        group_size = rabbits_seen + 1

        # Calculate the number of complete groups
        complete_groups = frequency // group_size

        # If some rabbits are left over,
        # another group is required
        if frequency % group_size == 0:
            minimum_count += complete_groups * group_size
        else:
            minimum_count += (complete_groups + 1) * group_size

    return minimum_count


# Driver code
rabbit_answers = [2, 2, 0, 0]
total_rabbits = len(rabbit_answers)

# Find and display the minimum number of rabbits
print(minimum_rabbits(rabbit_answers, total_rabbits))
