import emoji

class Jar:
    def __init__(self, size=0, capacity=12):
        self.size = size
        self.capacity = capacity

    def __str__(self):
        return f"{emoji.emojize(':cookie:') * self.size}"

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not (int(capacity) >= 0):
            raise ValueError
        self._capacity = capacity
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size


def main():
    cookie_jar = Jar()
    cookie_jar.deposit(11)
    cookie_jar.withdraw(3)
    print(cookie_jar)
    

if __name__ == "__main__":
    main()




