# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.items = [] #main stack to store all elements
        self.min_stack = [] # aux stack to track min val

    def push(self, val: int) -> None:
        self.items.append(val) #always push in main stack

        if not self.min_stack or val <= self.min_stack[-1]: #update min_stack 
            self.min_stack.append(val) # if min_stack is empty or val is less or equal to current min, push val

    def pop(self) -> None: 
        if not self.items:
            return None

        if self.items[-1] == self.min_stack[-1]:
            self.min_stack.pop()  # if the popped item is the current min, remove from min_stack
        
        return self.items.pop()

    def top(self) -> int:
        if not self.items:
            return None
        return self.items[-1]

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]

def test_min_stack():
    minStack = MinStack()
    
    operations = ["MinStack","push","push","push","getMin","pop","top","getMin"]
    inputs = [[],[-2],[0],[-3],[],[],[],[]]
    expected_output = [None,None,None,None,-3,None,0,-2]
    
    actual_output = [None]  # First None for MinStack initialization
    
    for op, val in zip(operations[1:], inputs[1:]):
        if op == "push":
            minStack.push(val[0])
            actual_output.append(None)
        elif op == "pop":
            minStack.pop()
            actual_output.append(None)
        elif op == "top":
            actual_output.append(minStack.top())
        elif op == "getMin":
            actual_output.append(minStack.getMin())
    
    print("Expected output:", expected_output)
    print("Actual output:  ", actual_output)
    assert actual_output == expected_output, "Test failed"
    print("Test passed successfully!")

test_min_stack()