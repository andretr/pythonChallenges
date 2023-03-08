# STACKS
stack = []
stack.append(1)
stack.append(2)

pop_elem = stack.pop()

print(stack, pop_elem)

# QUEUES
queue = [1, 2]

pop_elem = queue.pop(0)

print(queue, pop_elem)

# SETS
set1 = set([1, 2, 4, 6])
set2 = set([1, 3, 5, 6])

inter = set1 & set2

print(inter)

# DICTIONARYS
dict1 = dict()

dict1["A"] = "Apple"
dict1["B"] = "Banana"

for key, value in dict1.items():
    print(key, "->", value)

# List comprehension
lst = [1, 2, 3, 4, 5, 6, 7]

even_lst = [x for x in lst if x % 2 == 0]
print(f"Even: {even_lst}")

sqr_lst = [x ** 2 for x in lst]
print(sqr_lst)
