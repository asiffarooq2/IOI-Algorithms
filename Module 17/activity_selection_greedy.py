
def select_max_activities(start_times, finish_times):
    total_activities = len(finish_times)

    print("Selected activities:")

    # Select the first activity
    last_selected = 0
    print(last_selected, end=' ')

    # Check the remaining activities
    for activity_index in range(1, total_activities):

        # Select the activity if it starts after
        # or when the previous activity finishes
        if start_times[activity_index] >= finish_times[last_selected]:
            print(activity_index, end=' ')
            last_selected = activity_index


# Main program
if __name__ == '__main__':
    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]

    select_max_activities(start_times, finish_times)
