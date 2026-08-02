# ==========================================
# SEARCHING IN A DOUBLY LINKED LIST
# ==========================================


# Create a Node
class Node:

    def __init__(self, data):

        self.data = data

        # Address of previous node
        self.prev = None

        # Address of next node
        self.next = None


# Create Doubly Linked List
class DoublyLL:

    def __init__(self):

        self.head = None

    # Search for an element

    def searching(self, data):

        found = 0
        temp = self.head

        # Traverse through the linked list
        while temp:

            if temp.data == data:

                found = 1

                # Stop when element is found
                break

            temp = temp.next

        # Display search result
        if found == 1:

            print("Element Found")

        else:

            print("Element Not Found")

    # Display linked list

    def display(self):

        if self.head == None:

            print("List is empty")

        else:

            temp = self.head

            while temp:

                print(
                    temp.data,
                    "--->",
                    end=" "
                )

                temp = temp.next


# ==========================================
# DRIVER CODE
# ==========================================

linked_list = DoublyLL()


# Create nodes
node1 = Node(15)
linked_list.head = node1

node2 = Node(25)
node1.next = node2
node2.prev = node1

node3 = Node(35)
node2.next = node3
node3.prev = node2

node4 = Node(45)
node3.next = node4
node4.prev = node3


# Display linked list
print("Doubly Linked List:")

linked_list.display()


# Search for an element
print("\n\nSearching for 35:")

linked_list.searching(35)
