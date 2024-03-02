# enumarate function
# optional function
# makes working easier
# It returns both the index and the item corresponding to the index.

l1 = ['a', 'A', 'Ab', 'Abc']

i = 1
for item in l1:
    if i % 2 != 0:
        print(item)

for index, item in enumerate(l1):
    if index%2 == 0:
        print(item)