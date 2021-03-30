#Question 1


def hello_name(username):
	
	username = input("What is your user name? ")
	"""Hope the user responds to the input with 'General Kenobi.'"""
	print("Hello, there... " + username.title() + ".\n")
	
hello_name('username')


#Question2


for odd in range(1, 200, 2):
	print(odd)
	
	
#Question3
#Make space between questions.
print("\n")


def max_num_in_list(a_list):
	max = a_list[0]
	for a in a_list:
		if a > max:
			max = a
	return max
print(max_num_in_list([1, 2, 3, 4]))
	

#Question4
#Make space between questions.
print("\n")


def is_leap_year(a_year):
	return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)
print(is_leap_year(1900))


#Question5
#Make space between questions.
print("\n")


def if_consecutive(a_list):
	a_list = [a for a in range(a_list)]
	return a_list
print(if_consecutive(21))
