from DLL import DLL
import random

d = DLL()

r = random.randint(0, 100)

d.insert_after(random.random())
d.insert_after(random.random())
d.insert_after(random.random())
d.insert_after(random.random())
d.insert_after(random.random())

d.insert_before(r)
d.insert_before(random.randint(0, 100))
d.insert_before(random.randint(0, 100))
d.insert_before(random.randint(0, 100))
d.insert_before(random.randint(0, 100))

d.insert_after(random.randint(0, 100))
d.insert_after(random.randint(0, 100))
d.insert_after(random.randint(0, 100))
d.insert_after(random.randint(0, 100))

print(len(d))

for item in d:
    print(item.id, item.item_value)

print('\n\n\n\n')

d.remove_id(10)

print(len(d))

for item in d:
    print(item.id, item.item_value)

print('\n\n\n\n')

d.remove_id(14)

print(len(d))

for item in d:
    print(item.id, item.item_value)

print('\n\n\n\n')

d.remove_id(5)

print(len(d))

for item in d:
    print(item.id, item.item_value)


print('\n\n\n\n')

print(r)
d.remove_value(r)

print(len(d))

for item in d:
    print(item.id, item.item_value)
