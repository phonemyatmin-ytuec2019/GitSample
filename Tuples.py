#Tuple

Tuple - ()






t = 12345, 54321, 'hello!' #0,1,2
t[0]

# tuples can be nested
u = t, (1, 2, 3, 4, 5) # u[0],u[1]
u[1][2]# array of array


# tuples are immutable - can't change value
t[0] = 88888 # data can't be edited



# but Tuples can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
v

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])


# change Tuples value

x = ("apple", "banana", "cherry", "orange")
y = list(x)
y[1] = "mango"
x = tuple(y)
x


fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
x[4] = "pineapple"
fruits
>>> Set