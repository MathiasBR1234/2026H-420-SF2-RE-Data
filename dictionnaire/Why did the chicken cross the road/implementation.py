class Dict:
    def __init__(self, size = 100):
        self.values = [None]*size
    
    def hash(self, key):
        return hash(key) % len(self.values)
    
    def set(self, key, value):
        index = self.hash(key)
        i = 0
        while (not self.values[index+i] is None and
               not self.values[index+i][0] == key):
            i += 1
            if len(self.values) == index+i:
                raise MemoryError("Dictionary is full")
        self.values[index+i] = [key, value]
    
    def get(self, key):
        if not self.verify(key):
            raise KeyError("Key not found")
        index = self.hash(key)
        i = 0
        while not self.values[index+i][0] == key:
            i += 1
        return self.values[index+i][1]
    
    def delete(self, key):
        if not self.verify(key):
            raise KeyError("Key not found")
        index = self.hash(key)
        i = 0
        while not self.values[index+i][0] == key:
            i += 1
        self.values[index+i] = None

    def verify(self, key):
        index = self.hash(key)
        i = 0
        is_in_dict = True
        while (not self.values[index+i] is None and
               not self.values[index+i][0] == key):
            i += 1
            if index+i == len(self.values):
                is_in_dict = False
        if self.values[index+i] is None:
            is_in_dict = False
        return is_in_dict
    
test = Dict()
test.set("alibaba", "abc")
test.set("b", 2)
print(test.get("alibaba"))
print(test.get("b"))
print(test.verify("alibaba"))
print(test.verify("c"))
test.delete("alibaba")
print(test.verify("alibaba"))