# Flow Control

## 1. Intro

- Up until now, all the code we've written was executed in top-down order.
- Sometimes it's necessary to change the way a program flow, for example, making a program that can decide weather or not to run a piece of code.
- In Python, we have 3 flow control structures: if, for and while.


## 2. If

- If statements are Python's decision making structure.
- The decisions are made by checking the truth value of a condition.
- The blocks of code that are inside an If structure are only run if the condition is True.


- If Cheat Table
- | Operator | Meaning                  |
- |==========+==========================|
- | ==       | equality test            |
- |----------+--------------------------|
- | !=       | inequality test          |
- |----------+--------------------------|
- | >        | greater than             |
- |----------+--------------------------|
- | <        | less than                |
- |----------+--------------------------|
- | >=       | greater than or equal to |
- |----------+--------------------------|
- | <=       | less than or equal to    |
- |----------+--------------------------|
- | and      | logical and              |
- |----------+--------------------------|
- | or       | logical or               |
- |----------+--------------------------|
- | not      | logical not              |
- |----------+--------------------------|
- | True     | logical true             |
- |----------+--------------------------|
- | False    | logical false            |
- |----------+--------------------------|

- Usually If structures are followed by an optional Else clause.
- The code inside the Else clause is only ran if the condition in its corresponding If structure was False.

```python
#!/bin/python
day = int(input("Weekday? (1-7)"))
if day == 1 or day == 7: # You can test multiple condition at the same time
	print("Weekend")

else:
	print("Work day")
```

- If structures can be nested indefinitely (If structures inside If structures).
- We can also make use of Elif structures. These follow either another If or Elif structure and are just like an Else clause but with their own condition to test added.

```python
#!/bin/python
day = int(input("Weekday? (1-7)"))

if (day == 1): # Parentheses are optional
	print("Sunday")

elif day == 2:
	print("Monday")

elif day == 3:
	print("Tuesday")

elif day == 4:
	print("Wednesday")

elif day == 5:
	print("Thursday")

elif day == 6:
	print("Friday")

else:
	prinf("Saturday")
```

```python
#!/bin/python
number=123

guess = int(input("Your guess (tries left = 3)? "))
if number == guess:
	print("You got it right with 1 try!!")

else:
	guess = int(input("Your guess (tries left = 2)? "))
	if number == guess:
		print("You got it right with 2 tries!!")

	else:
		guess = int(input("Your guess (tries left = 1)? "))
		if number == guess:
			print("You got it right with 3 tries!!")

		else:
			print("You didn't manage to guess the number")
```


## 3. For
- The for loop is one of the two loops available in Python.
- We use this loop when we want to repeat a code block a known, finite, number of times
- The for loop makes heavy use of the range object.

- A range is defined as follows: range(start, [end, [step]]).
- The interval is closed on the left side and open on the right side [start, end).
- The step parameter is optional and by default is 1.
- We can also create range objects with only 1 parameter: range(3). These are the same as: range(0, 3).

```python
#!/bin/python
number=123

for i in range(3):
	guess = int(input("Your guess? "))
	if number == guess:
		print("You got it right!!")
		# We use the break keyword to end a loop early
		break

	else:
		print("Better luck next time.")
		# We use the continue keyword to go straight to the next loop iteration (just wanted to show it in this case)
		continue

if number != guess:
	print("You didn't manage to guess the number.")
```

- The for loop can be followed by an Else clause. The block of code inside the Else clause is executed once after the for loop is over, unless we reach a break keyword inside the for loop.

```python
#!/bin/python
number=123

for i in range(3):
	guess = int(input("Your guess? "))
	if number == guess:
		print("You got it right!!")
		# We use the break keyword to end a loop early
		break

	else:
		print("Better luck next time.")

else:
	print("You didn't manage to guess the number.")
```


## 4. While
- While is the second and last available loop in Python.
- We use this loop when we want to repeat a code for an unknown amount of times (while a condition is True).

```python
#!/bin/python
number = 123
choice = "yes"

guess = int(input("Your guess? "))

# Parantheses are optional
while (number != guess) and (choice == "yes"): # The tested condition works the same as in the If structure
	choice = input("You didn't get it right, would you like to try again? (yes/no) ")
	guess = int(input("Your guess? "))

if choice == "yes":
	print("You got it right!!")

else:
	print("Better luck next time.")
```

