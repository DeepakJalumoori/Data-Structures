class ListNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head_node = None

    def insert_at_index(self, index, value):
        """Insert a value at the specified index in the linked list."""
        if index < 0:
            raise IndexError("Index out of bounds")
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head_node
            self.head_node = new_node
            return
        current_node = self.head_node
        for _ in range(index - 1):
            if current_node is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    def delete_at_index(self, index):
        """Delete the node at the specified index in the linked list."""
        if index < 0:
            raise IndexError("Index out of bounds")
        if self.head_node is None:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head_node = self.head_node.next
            return
        current_node = self.head_node
        for _ in range(index - 1):
            if current_node.next is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next
        current_node.next = current_node.next.next

    def get_size(self):
        """Return the number of elements in the linked list."""
        count = 0
        current_node = self.head_node
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head_node is None

    def rotate_right(self, k):
        """Rotate the linked list to the right by k positions."""
        if not self.head_node or k == 0:
            return
        length = self.get_size()
        k = k % length
        if k == 0:
            return
        slow, fast = self.head_node, self.head_node
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = self.head_node
        self.head_node = new_head

    def reverse(self):
        """Reverse the order of elements in the linked list."""
        prev_node, current_node = None, self.head_node
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head_node = prev_node

    def append(self, value):
        """Append a value to the end of the linked list."""
        new_node = ListNode(value)
        if not self.head_node:
            self.head_node = new_node
            return
        current_node = self.head_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, value):
        """Prepend a value to the beginning of the linked list."""
        new_node = ListNode(value)
        new_node.next = self.head_node
        self.head_node = new_node

    def merge(self, other_list):
        """Merge another SingleLinkedList into this linked list."""
        if not self.head_node:
            self.head_node = other_list.head_node
            return
        current_node = self.head_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = other_list.head_node

    def interleave(self, other_list):
        """Interleave another SingleLinkedList with this linked list."""
        dummy_node = ListNode()
        tail = dummy_node
        l1, l2 = self.head_node, other_list.head_node
        while l1 or l2:
            if l1:
                tail.next = l1
                l1 = l1.next
                tail = tail.next
            if l2:
                tail.next = l2
                l2 = l2.next
                tail = tail.next
        self.head_node = dummy_node.next

    def get_middle(self):
        """Get the middle element of the linked list."""
        slow, fast = self.head_node, self.head_node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def index_of(self, value):
        """Return the index of the specified value in the linked list, or -1 if not found."""
        current_node = self.head_node
        index = 0
        while current_node:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def split_at_index(self, index):
        """Split the linked list at the specified index into two lists."""
        if index < 0:
            raise IndexError("Index out of bounds")
        if index == 0:
            new_list = SingleLinkedList()
            new_list.head_node = self.head_node
            self.head_node = None
            return new_list
        current_node = self.head_node
        for _ in range(index - 1):
            if current_node is None:
                raise IndexError("Index out of bounds")
            current_node = current_node.next
        new_list = SingleLinkedList()
        new_list.head_node = current_node.next
        current_node.next = None
        return new_list


# Initialize a SingleLinkedList
sll = SingleLinkedList()

# Append values
sll.append(1)
sll.append(2)
sll.append(3)

# Prepend a value
sll.prepend(0)

# Insert value at index
sll.insert_at_index(2, 1.5)

# Delete value at index
sll.delete_at_index(3)

# Rotate list right by 2 positions
sll.rotate_right(2)

# Reverse the list
sll.reverse()

# Merge with another SingleLinkedList
other_sll = SingleLinkedList()
other_sll.append(4)
other_sll.append(5)
sll.merge(other_sll)

# Interleave with another SingleLinkedList
interleaved_sll = SingleLinkedList()
interleaved_sll.append(6)
interleaved_sll.append(7)
sll.interleave(interleaved_sll)

# Get middle element
middle = sll.get_middle()

# Find index of a value
index = sll.index_of(2)

# Split the list at index
split_sll = sll.split_at_index(3)


