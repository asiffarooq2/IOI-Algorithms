
import heapq


# Function to schedule jobs and maximize profit
def schedule_jobs_by_profit(jobs):
    total_jobs = len(jobs)

    # Each job contains: job_id, deadline, profit

    # Sort jobs by deadline in ascending order
    jobs.sort(key=lambda job: job[1])

    # Store selected jobs and use a max-heap for profits
    scheduled_jobs = []
    max_profit_heap = []

    # Process jobs from the last deadline to the first
    for job_index in range(total_jobs - 1, -1, -1):

        # Calculate the available time slots
        if job_index == 0:
            available_slots = jobs[job_index][1]
        else:
            available_slots = (
                jobs[job_index][1] - jobs[job_index - 1][1]
            )

        # Add the job to the heap
        job_id = jobs[job_index][0]
        deadline = jobs[job_index][1]
        profit = jobs[job_index][2]

        # Negative profit converts Python's min-heap into a max-heap
        heapq.heappush(
            max_profit_heap,
            (-profit, deadline, job_id)
        )

        # Select the most profitable jobs for available slots
        while available_slots > 0 and max_profit_heap:
            negative_profit, job_deadline, selected_job_id = (
                heapq.heappop(max_profit_heap)
            )

            available_slots -= 1
            scheduled_jobs.append([selected_job_id, job_deadline])

    # Arrange selected jobs by deadline
    scheduled_jobs.sort(key=lambda job: job[1])

    # Display the job sequence
    for scheduled_job in scheduled_jobs:
        print(scheduled_job[0], end=" ")
    print()


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
    schedule_jobs_by_profit(jobs)
