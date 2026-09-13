# Python program to implement Queue using an Array


# Creating an array with maximum capacity
queue = [0 for _ in range(10)]
queue_size = 10

# Initializing front and rear
front_index = -1
rear_index = -1


# Function to perform Enqueue operation
def enqueue(element):
    global front_index, rear_index

    # Check for Overflow
    if rear_index == queue_size - 1:
        print("Overflow! Queue is full.")
        return

    # If queue is empty, set front and rear to 0
    if front_index == -1 and rear_index == -1:
        front_index = 0
        rear_index = 0
    else:
        rear_index += 1

    # Insert element at the rear
    queue[rear_index] = element
    print("Element inserted successfully.")


# Function to perform Dequeue operation
def dequeue():
    global front_index, rear_index

    # Check for Underflow
    if front_index == -1 or front_index > rear_index:
        print("Underflow! Queue is empty.")
        return

    # Store and display the deleted element
    deleted_element = queue[front_index]
    print("Element deleted from queue is:", deleted_element)

    # If only one element is present
    if front_index == rear_index:
        front_index = -1
        rear_index = -1
    else:
        front_index += 1


# Function to display all elements of the queue
def display_queue():
    if front_index == -1:
        print("Queue is empty.")
        return

    print("Queue elements are:", end=" ")

    current_index = front_index

    while current_index <= rear_index:
        print(queue[current_index], end=" ")
        current_index += 1

    print()


# Function to display the front element
def display_front():
    if front_index == -1:
        print("Queue is empty.")
        return

    print("Front element is:", queue[front_index])


# Main program
while True:

    print("\n----- Queue Menu -----")
    print("1. Insert element (Enqueue)")
    print("2. Delete element (Dequeue)")
    print("3. Display front element")
    print("4. Display all elements")
    print("5. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        element = int(input("Enter element to be inserted: "))
        enqueue(element)

    elif user_choice == 2:
        dequeue()

    elif user_choice == 3:
        display_front()

    elif user_choice == 4:
        display_queue()

    elif user_choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
