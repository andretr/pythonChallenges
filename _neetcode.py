# Variables are dynamicly typed
n = 0
print('n =', n)


n = "abc"
print('n =', n)


# Multiple assignments
n, m = 0, "abc"
n, m, z = 0.125, "abc", False

# Increment
n = n + 1 # good
n += 1    # good
# n++       # bad

# None is null (absence of value)
n = 4
n = None
print("n =", n)
# >>> n = None

#If
n = 2
if n > 4:
    n-=1
elif n == 3:
    n+=1
else:
    n = n**2

m = 0
if ((n == 4 and n%2 == 0)
        or n == m):
    print(f"n is even: {n}")
print(f"N: {n}")

n = 0
while n < 5:
    print(n)
    n += 1

print("range")
for i in range(2,6):
    print(i)
print("inv range")
for i in range(6,1,-1):
    print(i)

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

if __name__ == '__main__':
   print("Hello world!")

#MATRIX
rows = 3
columns = 2
mylist = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
    for j in range(columns):
        print(f"[{i}],[{j}]={mylist[i][j]}")

#REVERSE
# create a list of prime numbers
prime_numbers = [2, 3, 5, 7]
# reverse the order of list elements
print(prime_numbers.reverse())


def caesarCipher(s, k):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for idx in s:
        if idx not in alphabet:
            continue
        result += alphabet[(alphabet.index(idx) + k) % 26]
    return result


print(caesarCipher("wxyz", 4))
