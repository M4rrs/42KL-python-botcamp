def calculate( num1, oper, num2 ):
	if (oper == "+"):
			return num1 + num2
	elif (oper == "-"):
			return num1 - num2
	elif (oper == "*"):
			return num1 * num2
	elif (oper == "/"):
			return num1 / num2

print(calculate(10, "+", 10))
print(calculate(10, "-", 10))
print(calculate(10, "*", 10))
print(calculate(10, "/", 10))
