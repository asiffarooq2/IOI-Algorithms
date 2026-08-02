# ==========================================
# SINGLY LINKED LIST
# INSERT AT BEGINNING AND END
# ==========================================


# Create a Node
class Node:

    def __init__(self, data):

        self.data = data

        # Address of the next node
        self.next = None


# Create Singly Linked List
class SinglyLinkedList:

    def __init__(self):

        self.head = None


    # Insert a node at the beginning
    def insert_beg(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node


    # Insert a node at the end
    def insert_end(self, data):

        new_node = Node(data)

        temp = self.head

        while temp.next:

            temp = temp.next

        temp.next = new_node


    # Display the linked list
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

linked_list = SinglyLinkedList()


# Create initial nodes
node1 = Node(15)
linked_list.head = node1

node2 = Node(25)
node1.next = node2

node3 = Node(35)
node2.next = node3


# Display original linked list
print("Original Linked List:")

linked_list.display()


# Insert at beginning
linked_list.insert_beg(5)

print("\n\nAfter Inserting 5 at Beginning:")

linked_list.display()


# Insert at end
linked_list.insert_end(45)

print("\n\nAfter Inserting 45 at End:")

linked_list.display()