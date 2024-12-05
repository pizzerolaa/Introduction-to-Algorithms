from collections import deque

q = deque()

#enqueue O(1)
q.append(5)
q.append(4)
q.append(2)
print(q)

#dequeue O(1)
q.popleft()
print(q)