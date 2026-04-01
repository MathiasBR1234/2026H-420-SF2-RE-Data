class Stacks:
    def __init__(self, stack: list):
        self.stack = stack

    def poping(self):
        if self.sizstack == 0:
            print("Operation impossible: Stacks vide")
        else:
            return self.sizstack.pop()

    def push(self, donner):
        self.stack.append(donner)

    def peek(self):
        if self.sizstack == 0:
            print("Operation impossible: Stacks vide")
        else:
            return self.sizstack[-1]

    def sizstack(self):
        return len(self.stack)

    def __str__(self):
        return self.stack
