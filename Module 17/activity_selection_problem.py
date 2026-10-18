
def select_max_activities(activities):
    selected_activities = []

    # Sort activities by finish time
    activities.sort(key=lambda activity: activity[1])

    # Select the first activity
    last_selected_index = 0
    selected_activities.append(activities[last_selected_index])

    # Check the remaining activities
    for activity_index in range(1, len(activities)):

        # Select if the activity starts after the last one finishes
        if activities[activity_index][0] >= activities[last_selected_index][1]:
            selected_activities.append(activities[activity_index])
            last_selected_index = activity_index

    return selected_activities


# Main program
if __name__ == '__main__':
    activities = [
        [5, 9],
        [1, 2],
        [3, 4],
        [0, 6],
        [5, 7],
        [8, 9]
    ]

    selected_activities = select_max_activities(activities)

    print("Selected activities:")
    print(*selected_activities, sep=", ")
