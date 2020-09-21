class Node:
    def __init__(self, inputvalue):
        self.value = inputvalue
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        inputvalue = Node(value)
        if self.head == none:
            self.head = inputvalue
            self.tail = inputvalue
        else:
            self.tail.next = inputvalue
            self.tail = inputvalue
            return self

    def display(self):
    #some solution here that prints each value in a list
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next

            def     



            
            

