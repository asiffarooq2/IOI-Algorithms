
# Function to schedule jobs and maximize total profit
def schedule_jobs(jobs, max_time_slots):

    # Sort jobs by profit in descending order
    jobs.sort(key=lambda job: job[2], reverse=True)

    # Track which time slots are occupied
    occupied_slots = [False] * max_time_slots

    # Store the scheduled job IDs
    scheduled_jobs = ['-1'] * max_time_slots

    # Process jobs in order of highest profit
    for job in jobs:

        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        # Find the latest available slot before the deadline
        for slot in range(
            min(max_time_slots, deadline) - 1, -1, -1
        ):

            # Schedule the job if the slot is free
            if not occupied_slots[slot]:
                occupied_slots[slot] = True
                scheduled_jobs[slot] = job_id
                break

    # Display the scheduled jobs
    print("Scheduled jobs:", scheduled_jobs)


# Main program
if __name__ == '__main__':

    jobs = [
        ['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]
    ]

    print("Maximum profit job sequence:")

    schedule_jobs(jobs, 3)
