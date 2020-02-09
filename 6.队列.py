

# from queue import LifoQueue
# q=LifoQueue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.put(4)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())

from queue import PriorityQueue
q=PriorityQueue()
q.put((10,'luwei'))
q.put((5,'yaoting'))
q.put((15,'ting'))

print(q.get())
print(q.get())
print(q.get())
