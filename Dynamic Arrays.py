class DynamicArray:
    def __init__(self, growth_factor=2):
        self.data = []
        self.current_size = 0
        self.growth_factor = growth_factor

    def _resize(self, new_capacity):
        """Resize the internal storage array to the new capacity."""
        new_data = [None] * new_capacity
        for i in range(self.current_size):
            new_data[i] = self.data[i]
        self.data = new_data

    def insert_at_index(self, index, value):
        """Insert a value at the specified index."""
        if index < 0 or index > self.current_size:
            raise IndexError("Index out of bounds")
        if self.current_size == len(self.data):
            self._resize(max(1, len(self.data) * self.growth_factor))
        for i in range(self.current_size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.current_size += 1

    def delete_at_index(self, index):
        """Delete the value at the specified index."""
        if index < 0 or index >= self.current_size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.current_size - 1):
            self.data[i] = self.data[i + 1]
        self.current_size -= 1
        self.data[self.current_size] = None
        if self.current_size <= len(self.data) // (self.growth_factor * 2):
            self._resize(max(1, len(self.data) // self.growth_factor))

    def get_size(self):
        """Return the number of elements in the array."""
        return self.current_size

    def is_empty(self):
        """Check if the array is empty."""
        return self.current_size == 0

    def rotate_right(self, k):
        """Rotate the array to the right by k positions."""
        if self.current_size == 0 or k == 0:
            return
        k = k % self.current_size
        self.data = self.data[-k:] + self.data[:-k]

    def reverse(self):
        """Reverse the order of elements in the array."""
        left, right = 0, self.current_size - 1
        while left < right:
            self.data[left], self.data[right] = self.data[right], self.data[left]
            left += 1
            right -= 1

    def append(self, value):
        """Append a value to the end of the array."""
        if self.current_size == len(self.data):
            self._resize(max(1, len(self.data) * self.growth_factor))
        self.data[self.current_size] = value
        self.current_size += 1

    def prepend(self, value):
        """Prepend a value to the beginning of the array."""
        self.insert_at_index(0, value)

    def merge(self, other):
        """Merge another DynamicArray into this array."""
        for element in other.data[:other.current_size]:
            self.append(element)

    def interleave(self, other):
        """Interleave another DynamicArray with this array and return the result."""
        new_array = DynamicArray()
        i, j = 0, 0
        while i < self.current_size or j < other.current_size:
            if i < self.current_size:
                new_array.append(self.data[i])
                i += 1
            if j < other.current_size:
                new_array.append(other.data[j])
                j += 1
        return new_array

    def get_middle(self):
        """Get the middle element of the array."""
        if self.current_size == 0:
            return None
        return self.data[self.current_size // 2]

    def index_of(self, value):
        """Return the index of the specified value, or -1 if not found."""
        for i in range(self.current_size):
            if self.data[i] == value:
                return i
        return -1

    def split_at_index(self, index):
        """Split the array at the specified index into two arrays."""
        if index < 0 or index > self.current_size:
            raise IndexError("Index out of bounds")
        first_part = DynamicArray()
        second_part = DynamicArray()
        for i in range(index):
            first_part.append(self.data[i])
        for i in range(index, self.current_size):
            second_part.append(self.data[i])
        return first_part, second_part


# Example usage:

# Initialize a DynamicArray
da = DynamicArray()

# Append values
da.append(1)
da.append(2)
da.append(3)

# Prepend a value
da.prepend(0)

# Insert value at index
da.insert_at_index(2, 1.5)

# Delete value at index
da.delete_at_index(3)

# Rotate array right by 2 positions
da.rotate_right(2)

# Reverse the array
da.reverse()

# Merge with another DynamicArray
other_da = DynamicArray()
other_da.append(4)
other_da.append(5)
da.merge(other_da)

# Interleave with another DynamicArray
interleaved_da = da.interleave(other_da)

# Get middle element
middle = da.get_middle()

# Find index of a value
index = da.index_of(2)

# Split the array at index
first_part, second_part = da.split_at_index(3)
