# 1 - Hello!  
Create some Python code that will prompt you to enter your name and age. Print out Hello
and then the name followed by how old they'll be next year.  
```
input:
	Jorge
	21
output:
	Hello Jorge!
	Next year you'll be 22.
```

# 2 - Odd or Even?  
Write some code that checks whether or not a given number is odd or even and prints "Odd" or "Even" accordingly.  
```
input:
	3
output:
	Odd
```

# 3 - Octal 
Implement some Python code that converts a given number in base 10 to base 8 (octal) using at least 1 'for loop'.
```
input:
	9
output:
	10
```

# 4 - The string's classic 
Assume that everyone has 1 first name and at least 1 last name. Write a python program that given someones name prints it according to the following rules:  
Note: you may find the .split method useful.  
- The first name stays as is.  
- Middle names are abbreviated to only the first letter and a dot.
- The last name stays as is.
```
input:
	Maria Manuel Saavedra
output:
	Maria M. Saavedra
```

# 5 - Case converter
Write a function that takes camel cased strings (i.e. ThisIsCamelCased), and converts them to snake case (i.e. this_is_camel_cased).  
Modify the function by adding an argument, separator, so it will also convert to kebab case (i.e. this-is-camel-case) as well.  
```
input:
	ThisIsCamelCased
output:
	this_is_camel_cased
```

# 6 - Sort and comparison functions  
a) Instantiate a python list object. Read an integer, n, that represents the number of tuples you're gonna read next (each tuple is comprised of 1 string and 1 float). Each tuple you read, will have to be appended to the list you instantiated.  
Print the last element of your list object (note: you may try out the index -1 in your list to get the last element).  
```
input:
	3
	Joao 21.3
	Cucs 912.4
	Tiago 22.6
output:
	Tiago 22.6
```
b) Now try using the built-in "sorted" function to sort your list in ascending order, considering only the floats, before printing the last element of the list. For this, you'll need to define a comparison function that takes 2 tuples as arguments and returns:  
- true if the float of the second tuple is greater than or equal to the float of the first tuple.
- false otherwise.
```
input:
	3
	Joao 21.3
	Cucs 912.4
	Tiago 22.6
output:
	Cucs 912.4
```

# 7 - Anagrams
Write Python code that will print the anagrams (words made from the same letters) from a paragraph of text.  
```
input:
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
	Vestibulum venenatis gravida orci vel pellentesque.  
	Nunc sodales quis felis ac gravida.  
	Maecenas iaculis aliquam mauris, eu hendrerit dui mattis nec.  
	Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
	Praesent congue libero sed purus consequat posuere. Sed quis neque elit.  
	Aliquam vitae facilisis urna.	
output:
	//TODO
```
