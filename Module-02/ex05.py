def check_string( str ):
	if (str.startswith("The")):
		return "Yes!"
	else:
		return "No!"

str1 = "The"
str2 = "Thumbs up"
str3 = "Theatre"

print(check_string(str1))
print(check_string(str2))
print(check_string(str3))