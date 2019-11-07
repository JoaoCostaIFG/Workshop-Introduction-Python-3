template: slide_section
name: data_structures
# Data Structures

---

template: slide_normal
## Intro
Variables have already shown to be extremely useful in many situations but sometimes they are not enough. We'll now talk about Python's standard data structures and show how/why they can be useful in many situations.

In Python, we have 4 standard data structures:  
1. [Lists](#lists)  
1. [Tuples](#tuples)  
1. [Sets](#sets)  
1. [Dictionaries](#dictionaries)  


## Lists

**Lists** are one of/the most commonly used data structure in Python. A **List** is an **ordered**, **mutable** sequence of elements. Each element inside a **List** is called an **item**.  
- The **items** are indexed by an integer starting on 0.  
- In Python, the **items** are also be indexed by a negative integer that starts in -1 on the last item of the **List**.  
- **Lists** usually contain only **items** of the same type (this type can be **List** so we can have nested **Lists**).  
- You can cast iterable objects to the **List** type using: `alist = list(iterable)`

<p align="center">
   <img src="http://www.nltk.org/images/string-slicing.png" alt="list indexing (Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.)" width="auto" height="200px"/>
</p>

#### Example

```python
# Declare a list with the items 1, 2
alist = [1, 2]
print("Our list:", alist)

# Appends an element to the end of the list
alist.append(5)
print("Our list:", alist)

# Appends all the elements in an iterable to 'alist'
anotherlist = [3, 4]
alist.extend(anotherlist)
print("Our list:", alist)

# Inserts an item, x, at a given position, i, in a list (list.insert(i,x))
alist.insert(1, 9)
print("Our List:", alist)

# Removes the first item from the list with value x (list.remove(x))
alist.remove(9)
print("Our List:", alist)

# Remove and return an item from a list at a given position, i
# If no argument is given, remove and return the last element from the list
alist.pop(1)
print("Our List:", alist)

# Return the index of the first item with value x in the list
# Can take an option start and/or end index (list.index(x[, start[, end]]))
print("Index:", alist.index(1))

# Count the number of times an item, x, appears in the list
print("Number of occurrences", alist.count(1))

# Reverses the items of the list, in place
alist.reverse()
print("Our list:", alist)

# blist is a pointer to alist
blist = alist
# blist is a shallow copy of alist (doesn't 'shallow copy' recursively)
blist = alist.copy()

# remove all items from a list (equivalent to del alist[:] (see next section))
print("Our list:", blist)
blist.clear()
print("Our list:", blist)
```

As you might as noticed, **Strings** and **Lists** have many common properties, like indexing and slicing operations. The are both examples of sequence data types.  
Methods that only modify the **List** have return value **None**. This is a design principle for all **mutable** data structures in **Python**.  

#### The del statement

- We can use the **del** statement to remove an item from a list given its index.  
- The **del** statement differs from the **pop()** method because it doesn't return a value.  
- The **del** statement can also be used to remove **slices** of items from a list (including clearing the whole list).  

```python
alist = [1, 2, 3, 4, 5, 6, 7, 8]
print("Our list:", alist)

# Remove 1 element
del alist[1]
print("Our list:", alist)

# Remove a slice
del alist[0:3]
print("Our list:", alist)

# Remove all elements (same as alist.clear())
del alist[:]
print("Our list:", alist)
```


## Tuples

**Tuples** are another of **Python's** standard sequence data types. They are an **ordered**, **immutable** data structure.  
- The indexing starts at 0.  
- **Tuples** can, and usually, contain elements of any type and of different types (heterogeneous elements).  
- **Tuples** can be nested.  
- If a **Tuple** contains an **mutable** object, we can still change the objects value which in turn 'change' the **Tuple**.  
- It is not possible to assign to any of the individual items of a tuple. The assignment is made during the declaration of the **Tuple**.  
- You can cast iterable objects to the **Tuple** type using: `atuple = tuple(iterable)`

#### Example

```python
# The paratheses are not mandatory in most declarations but we recommend their use either way
atuple = (1, 2, 'hey', 4.2, 0)

# Print the whole tuple
print("Our tuple:", atuple)

# Elements are indexed
print("1st element of out tuple", atuple[0])

# Nested tuples
btuple = ("a", atuple, 96, atuple)
print("Our nested tuple:", btuple)

# Since tuples are immutable, this next commented line results in an error
# atuple[1] = 3

# But they can contain mutable objects
alist = [1, 2, 3]
ctuple = (alist, 4, 5)
print("Our ctuple:", ctuple)

ctuple[0][0] = 3
print("Our ctuple:", ctuple)
```

#### Special Tuples

Sometimes, we may find ourselves in need of creating a **Tuple** with 1 or 0 elements. To do this, we need to use a slightly more confusing syntax.

```python
# Declare an empty tuple
emptytuple = ()

# Declare a tuple with only 1 element
singletuple = (1, )  # Notice the trailing comma

print("Our tuples:", emptytuple, singletuple)

print("emptytuple's len:", len(emptytuple))
print("singletuple:", len(singletuple))
```

#### Sequence Unpacking

We can use **Tuples** to pack/unpack sequences. Sequence unpacking requires us to give the same number of variables on the left side of the equal sign as elements inside the **Tuple**.

```python
# Tuple packing
atuple = (1, "hey", 123412.32)
print("Our tuple", atuple)

# Sequence unpacking (paretheses are also optional here)
(x, y, z) = atuple
print("Our varibles:", x, y, z)
```


## Sets

**Sets** are **unordered** collections of elements with **no duplicates**. Basic uses include membership testing and eliminating duplicate entries.  
Mathematical operations like union, intersection, difference, and symmetric difference.  
- **Sets'** elements aren't indexed and we can't rely on them being in any specific order.  
- To create a **Set**, we can use curly braces or the `set()` function. We should note that we can't do: `emptyset = {}` in order to create an empty set, as this would create an empty **[Dictionary](#dictionaries)**. To create an empty **Set**, we use: `emptyset = set()`.  
- The `set()` function can also be used to cast an iterable to the **Set** type: `aset = set(iterable)`.  

```python
# Declare a set
aset = {"yum", "sweet", "potato", "yum"}
# Equivalent to aset = set(['yum', 'sweet', 'potato'])
print("Our set:", aset)

# Check membership
# This in keyword will be discussed in detail in the chapter about iterables
# For now, we just need to know that it checks if "yum" is equal to at least 1 of the elements of aset
print("yum" in aset)
print("Iargo" in aset)


# Crating sets from an iterable (string)
x = set("comparable")
y = set("complementary")

# Unique letters
print("Unique letters in x:", x)
print("Unique letters in y:", y)

# Difference
print("Letters in x but nor in y:", x - y)

# Union (Or)
print("Letters in x, y or both:", x | y)

# Intersection (And)
print("Letter in both x and y:", x & y)

# Symmetric difference (Xor)
print("Letters in x or y but not in both:", x ^ y)
```


## Dictionaries

**Dictionaries** are the last standard data structure we're gonna talk about in **Python**. It's usual for this to be called 'associative memories' or 'associative arrays' in other languages.  
The biggest difference between a sequence data type, like **[Lists](#lists)** or **[Tuples](#tuples)**, which are indexed by a range of integers, and **Dictionaries** is that Dictionaries are indexed by **keys**.  
- **Keys** can be of any **immutable** type. **Strings** and **numbers** can always be keys.  
- **[Tuples](#tuples)** can be used as **keys** if they only contain strings, numbers or **[Tuples](#tuples)**. If a **[Tuples](#tuples)** contains any mutable object, either directly or indirectly, it can't be used as a **key**.  

**Dictionaries** store **key:value** pairs. We can't have duplicated **keys** but we can have 2 different **keys** associated with the same **value**.  
**Dictionaries** can be declared using {} or using the dict() function (by casting a nest iterable).  

```python
# Examples a dictionary declaration that associates names with age
# Equivalent to ages = dict([[Carlos, 12], [Vilas, 19], [Tiago, 5]])
# Or, since the keys are all simple strings, ages = dict(Carlos=12, Vilas=19, Tiago=5)
ages = {"Carlos": 12, "Vilas": 19, "Tiago": 5}
print("Our dict:", ages)

# Print a single element
print("Tiago's age:", ages["Tiago"])

# We can add any key:value pair to dictionary at any time
ages[432.5] = "oops"
print("Our dict:", ages)

# The list() funtion will return a list of the keys in the dictionary in insertion order
print("Our keys list:", list(ages))

# The values() method will return an object of type dict_values
# with a list of the values in the dictionary in insertion order
print("Our values list:", list(ages.values()))

# A dictionary is also an iterable (will be discussed in the iterable chapter)
print("Carlos" in ages)

# The next commented line results in an order because we can't access non-existant keys
# print(ages["123"])

# If we store a key that's already in use, the previous value of that key is dropped
ages["Carlos"] = 11
print("Our dict:", ages)

# We can use the del keyword with dictionaries
del ages["Vilas"]
print("Our dict:", ages)
```

#### Sections

Previous: [Flow Control](Flow-Control)  
Next: [Iteration](Iteration)  
