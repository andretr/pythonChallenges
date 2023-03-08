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