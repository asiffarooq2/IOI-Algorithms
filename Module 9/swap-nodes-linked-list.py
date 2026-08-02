# ==========================================
# SWAP NODES IN A SINGLY LINKED LIST
# ==========================================


# Create a Node
class Node:

    def __init__(self, data):

        self.data = data

        # Address of the next node
        self.next = None


# Create Singly Linked List
class SinglyLL:

    def __init__(self):

        self.head = None

    # Swap two given nodes

    def swap(self, value1, value2):

        prevNode1 = None
        prevNode2 = None

        node1 = self.head
        node2 = self.head

        # Check if list is empty
        if self.head == None:
            return

        # If both values are same,
        # no swapping is required
        if value1 == value2:
            return

        # Search for first node
        while node1 != None and node1.data != value1:

            prevNode1 = node1
            node1 = node1.next

        # Search for second node
        while node2 != None and node2.data != value2:

            prevNode2 = node2
            node2 = node2.next

        # Check if both nodes exist
        if node1 != None and node2 != None:

            # Connect previous node of
            # node1 with node2
            if prevNode1 != None:

                prevNode1.next = node2

            else:

                self.head = node2

            # Connect previous node of
            # node2 with node1
            if prevNode2 != None:

                prevNode2.next = node1

            else:

                self.head = node1

            # Swap next addresses
            temp = node1.next

            node1.next = node2.next

            node2.next = temp

        else:

            print("Swapping is not possible!")

    # Display linked list

    def display(self):

        if self.head == None:

            print("List is empty")

        else:

            temp = self.head

            while temp:

                print(
                    temp.data,
                    "-->",
                    end=" "
                )

                temp = temp.next


# ==========================================
# DRIVER CODE
# ==========================================

linked_list = SinglyLL()


# Create nodes
node1 = Node(15)
linked_list.head = node1

node2 = Node(25)
node1.next = node2

node3 = Node(35)
node2.next = node3

node4 = Node(45)
node3.next = node4


# Display original linked list
print("Original Linked List:")

linked_list.display()


# Swap nodes containing 15 and 35
linked_list.swap(15, 35)


# Display list after swapping
print("\n\nAfter Swapping 15 and 35:")

linked_list.display()
