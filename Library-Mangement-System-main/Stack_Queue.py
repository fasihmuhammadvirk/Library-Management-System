from collections import deque

#class containing all the needed function of a queue
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self,val):
      self.buffer.appendleft(val)
    def deqeue(self):
      if len(self.buffer) == 0:
        print(
            '''
     |----------------|
     | Queue is Empty |
     |----------------|\n
            '''
            )
        return
      return self.buffer.pop()
    def is_empty(self):
      return len(self.buffer) == 0
    def size(self):
      return len(self.buffer)
    def front(self):
      return self.buffer[-1]
    def ListofRequests(self):
        if self.is_empty():
            print(
                '''
     |-------------------------|
     | No Request at this time |
     |-------------------------|\n''')
        else:
            for i in range(self.size()):
                item = -1
                for i in range(self.size()):
                    print(
                       f'''
     |---------------------------------------------------------|
     | The  {i + 1} Request on The list is {self.buffer[item]} |
     |---------------------------------------------------------|\n
                        ''')
                    item -= 1

    def Requests(self):
        item = -1
        for i in range(self.size()):
             print(
                f'''
     |--------------------------------------------------------------|
     | You are at {i + 1 } on list {self.buffer[item]}              | 
     | Kindly Wait for Your Turn Book will be issued to you Shortly |
     |--------------------------------------------------------------|\n
                ''')

             item -= 1

#class contaning all the needne functions of the stack
class Stack:
    def __init__(self):
        self.stack = deque()
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        self.stack.pop()
    def isempty(self):
        if self.size() == 0:
            return True
        else:
            False
    def size(self):
        return len(self.stack)
