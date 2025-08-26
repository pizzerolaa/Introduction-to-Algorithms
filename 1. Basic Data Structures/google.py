import random

class store:
    def __init__(self) -> None:
        self.map = set()
    
    def insert(self, value):
        self.map.add(value)
    
    def delete(self, value):
        self.map.remove(value)
    
    def get_random_value(self):
        return random.choice(list(self.map))
    
my_store = store()
my_store.insert(3)
my_store.insert(5)
my_store.insert(4)
my_store.insert(2)
my_store.insert(1)

print(my_store.get_random_value())
print(my_store.map)

my_store.delete(2)
print(my_store.map)
