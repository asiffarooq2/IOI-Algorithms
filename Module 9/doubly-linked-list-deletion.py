# ==========================================
# DOUBLY LINKED LIST
# DELETE FROM BEGINNING AND END
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

    # Delete node from beginning

    def delete_beg(self):

        if self.head != None:

            temp = self.head

            self.head = self.head.next

            # If list is not empty after deletion
            if self.head != None:
                self.head.prev = None

            temp = None

    # Delete node from end

    def delete_end(self):

        if self.head != None:

            # If only one node exists
            if self.head.next == None:

                self.head = None

            else:

                temp = self.head

                # Move to second-last node
                while temp.next.next:

                    temp = temp.next

                # Remove the last node
                temp.next = None

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

node4 = Node(45)
node3.next = node4
node4.prev = node3


# Display original list
print("Original Doubly Linked List:")
linked_list.display()


# Delete from beginning
linked_list.delete_beg()

print("\n\nAfter Deleting From Beginning:")
linked_list.display()


# Delete from end
linked_list.delete_end()

print("\n\nAfter Deleting From End:")
linked_list.display()
