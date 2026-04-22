class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def add(self, value):
        if value <= self.value:
            if self.left is None:
                self.right = TreeNode(value)
            else:
                self.right.add(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.add(value)
    
    def remove(self, value):
        if value == self.value:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                temp = self.left
                self.left = None
                return temp
        
        elif value < self.value:
            self.left = self.left.remove(value)

        else:
            self.right = self.right.remove(value)
    
    def search(self, value, node = 0):
        if value == self.value:
            return node+1
        elif value < self.value:
            if self.left is None:
                raise KeyError("Value not found")
            else:
                return self.left.search(value, node+1)
        else:
            if self.right is None:
                raise KeyError("Value not found")
            else:
                return self.right.search(value, node+1)
    
    def content(self):
        res = []
        if (self.left is None and 
            self.right is None):
            res.append(self.value)

        elif self.left is None:
            res.append(self.value)
            res.extend(self.right.content())
        
        elif self.right is None:
            res.extend(self.left.content())
            res.append(self.value)
        
        else:
            res.extend(self.left.content())
            res.append(self.value)
            res.extend(self.right.content())
        
        return res
    
    def height(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return 1 + self.right.height()
        elif self.right is None:
            return 1 + self.left.height()
        else:
            return sum([1, max(self.left.height(), self.right.height())])