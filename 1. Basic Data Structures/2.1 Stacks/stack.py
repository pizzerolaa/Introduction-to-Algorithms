from typing import List
class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, num: int) -> None:
        self.items.append(num)
    
    def pop(self) -> int:
        if self.is_empty():
            return -1
        num = self.items[-1]
        self.items.pop()
        return num
    
    def peek(self) -> int:
        if self.is_empty():
            return -1
        return self.items[-1]
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def size(self) -> int:
        return len(self.items)
    
    def __str__(self) -> str:
        return f"Stack({self.items})"
    
def main():
    s = Stack()
    s.push(2)
    s.push(4)
    s.push(5)
    s.push(6)
    s.pop()
    ss = s.is_empty()
    var = s.peek()
    size = s.size()

    print(s)
    print(ss)
    print(var)
    print(size)

main()