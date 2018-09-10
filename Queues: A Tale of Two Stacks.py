class MyQueue(object):
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []
    
    def peek(self):
        if len(self.stack_pop) == 0:
            while len(self.stack_push) > 0:
                self.stack_pop.append(self.stack_push.pop())
        return self.stack_pop[-1]
        
    def pop(self):
        if len(self.stack_pop) == 0:
            while len(self.stack_push) > 0:
                self.stack_pop.append(self.stack_push.pop())
        self.stack_pop.pop()
        
    def put(self, value):
        self.stack_push.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
