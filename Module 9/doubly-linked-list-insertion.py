# ==========================================
# DOUBLY LINKED LIST
# INSERT AT BEGINNING AND END
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

    # Insert node at beginning

    def insert_beg(self, data):

        new_node = Node(data)

        new_node.next = self.head

        # Connect old head back to new node
        if self.head != None:
            self.head.prev = new_node

        self.head = new_node

    # Insert node at end

    def insert_end(self, data):

        new_node = Node(data)

        # Handle empty list
        if self.head == None:
            self.head = new_node
            return

        temp = self.head

        # Move to last node
        while temp.next:

            temp = temp.next

        # Connect new node
        temp.next = new_node
        new_node.prev = temp

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


# Create initial nodes
node1 = Node(15)
linked_list.head = node1

node2 = Node(25)
node1.next = node2
node2.prev = node1

node3 = Node(35)
node2.next = node3
node3.prev = node2


# Display original list
print("Original Doubly Linked List:")
linked_list.display()


# Insert at beginning
linked_list.insert_beg(5)

print("\n\nAfter Inserting 5 at Beginning:")
linked_list.display()


# Insert at end
linked_list.insert_end(45)

print("\n\nAfter Inserting 45 at End:")
linked_list.display()
