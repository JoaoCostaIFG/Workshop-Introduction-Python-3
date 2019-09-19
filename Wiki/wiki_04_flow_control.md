# Flow Control
-Intro
	-Ate agora tudo o que fizemos e executado em top-down order.
	-Por vezes e necessario mudar a forma como o programa flui, por exemplo, fazer com que o programa tome decisoes sobre qual caminho tomar dependo da situacao.
	-Em python temos 3 statements de controlo do fluxo: if, for e while.


-If
	-O If statement e usado para verficar a veracidade de uma condicao.
	-Os blocos de codigo que colocarmos dentro de um If statement so sao executados se a condicao que fornecermos se verificar.

	| Operator | Meaning                  |
	|==========+==========================|
	| ==       | equality test            |
	|----------+--------------------------|
	| !=       | inequality test          |
	|----------+--------------------------|
	| >        | greater than             |
	|----------+--------------------------|
	| <        | less than                |
	|----------+--------------------------|
	| >=       | greater than or equal to |
	|----------+--------------------------|
	| <=       | less than or equal to    |
	|----------+--------------------------|
	| and      | logical and              |
	|----------+--------------------------|
	| or       | logical or               |
	|----------+--------------------------|
	| not      | logical not              |
	|----------+--------------------------|
	| True     | logical true             |
	|----------+--------------------------|
	| False    | logical false            |
	|----------+--------------------------|

	-E usual que os if statements sejam seguidos de um Else (e opcional).
	-Os blocos de codigo que colocarmos dentro de um Else statement so sao executados se a condicao testada no If statement que lhe corresponde nao se verificar.

	#!/bin/python
	day = int(input("Weekday? (1-7)"))
	if day == 1 or day == 7:
		print("Weekend")

	else:
		print("Work day")

	-E possivel criar nested If statements, isto e, colocar If statements dentro do bloco de codigo de um If statement.
	-Tambem e existem Elif statements. Estes parecem em seguimento de um If ou de um Elif statement e funcionam da mesma forma que um If statement.

	#!/bin/python
	day = int(input("Weekday? (1-7)"))
	if day == 1:
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


-For
	-The for loop is one of the two loops available in python.
	-We use this loop when we want to repeat a code block a known, finite, number of times
	-The for loop makes heavy use of the range object.
	-A range is defined as follows: range(start, [end, [step]]).
	-The end parameter is optional and the interval is closed on the left side and open on the right side [start).
	-The step parameter is optional and by default is 1.

	#!/bin/python
	number=123

	for i in range(3):
		guess = int(input("Your guess? "))
		if number == guess:
			print("You got it right!!")

	if number != guess:
		print("You didn't manage to guess the number")


	-The for loop can be followed by an else statement. The block of code inside de else statement is executed once after the for loop is over, unless we reach a break keyword inside the for loop.
	-We can use the break keyword to exit out of a for loop early.

	#!/bin/python
	number = 123
	flag = True

	for i in range(3):
		guess = int(input("Your guess? "))
		if number == guess:
			flag = False
			break

	else:
		print("You didn't manage to guess the number")

	if flag:
		print("You got it right!!")

