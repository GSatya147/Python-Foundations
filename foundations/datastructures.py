 # LISTS - ordered, mutable

list1 = ["one", "two", "three", 3]
lst2 = [1, 2, 3]

#slicing and indexing works the same list1[slicing, indexing]

# lists methods
len(list1)
list1.append("four")
list1.insert(0, "four")

list1.insert(0, lst2) # add lst as a list in first pos, making length 5
list1.append(lst2) # adds lst2 as a list item making length 5
list1.extend(lst2) # blends both lists, making length 7

list1.remove("two") # removes in-place
a = list1.pop() # pops last element and also returns it

# in-place
list1.reverse()
list1.sort(revrse = True) # by default ascending order

sorted_list = sorted(list1) # returns a sorted list

# functions
min(list1)
max(list1)
sum(list1)

list1.index("four") # returns value error for absent items
"four" in list1 # returns boolean

# iterating
for i in list1:
    print(i)

for i, j in enumerate(list1): # by default 0
    print(f"{i}: {j}")

for i, j in enumerate(list1, start = 1):
    print(f"{i}: {j}")

# join
list1_str = ' - '.join(list1) # returns one - two - three..

# split
new_list = list1_str.split(" - ")


# TUPLES - ordered, immutable
tuple = (1, 2, 3, 4)
tuple1 = (1, )

# SETS - distinct, unordered
set1 = {1, 2, 3, 4} 
set2 = {2, 5, 6, 7}

# lookups are more efficient in sets
1 in set1

# set math
set1.intersection(set2)
set1.difference(set2) # set1 - set2
set1.union(set2)

# EMPTY
empty_list = []
empty_list = list()

empty_tup = ()
empty_tup = tuple()

empty_set = {} # this is a dictionary
empty_set = set() 

# DICTIONARY 
student = {
    "name": "satya",
    "age" : 22 # keys can be any immutable datatypes, int, tuples inlcuded
}

# Accessing
student["name"] # retuns key error for absent keys
student.get("name") # returns none by default for unavailable
student.get("name", "Not Found") # retuns Not Found for unavailable

# can update
student["name"] = 'veera'

# can add
student["phone"] = 44

# takes dict as arg
student.update({"name": "veera", "phone": 44})

# delete
del student["age"]
age = student.pop("age") # returns value

student.keys()
student.values()
student.items() # returns list of tuples of (keys, values)

# iterating
i in student.keys()
i in student.values()
i, j in student.items()