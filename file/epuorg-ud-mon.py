class Queues:
    def __init__(self, queue: list):
        self.queue = queue

    def poping(self):
        if self.sizstack == 0:
            print("Operation impossible: Queue vide")
        else:
            nbr_pop = self.Queue[0]
            self.Queue = self.Queue[1:]
            return nbr_pop

    def push(self, donner):
        self.Queue.append(donner)

    def peek(self):
        if self.sizstack == 0:
            print("Operation impossible: Queue vide")
        else:
            return self.sizstack[-1]

    def sizstack(self):
        return len(self.Queue)

    def __str__(self):
        return self.Queue
