class Jar:
    def __init__(self, capacity=12): #Set the maximum capacity, 12 by default
        self.capacity = capacity
        self._size = 0 #Set 0 cookies currently in the jar

    def __str__(self): #Print the number of cookies in the jar
        return ("🍪" * self._size)

    def deposit(self, n): #Add n cookies to the jar
        self.size += n

    def withdraw(self, n): # take n cookies from the jar
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter #check the current capacity value
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter #check the current size value
    def size(self, size):
        if size < 0 or size > self._capacity:
            raise ValueError
        self._size = size
