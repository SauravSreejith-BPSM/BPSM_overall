#! /bin/user/python3


import os


def questions(name,age,colour,python,world):
	if age<2 or age>90:
		print("Wonderful")
	else:
		print("Thank you")
	if colour=="white" or colour=="black":
		print("Basic")
	else:
		print("Great choice")
	if python=="Yes":
		print("Al would be proud")
	else:
		print("Al would be dissapointed")
	if world=="TRUE":
		print("Smart choice")
	else:
		print("Need to touch grass")
	return "Thank"


question={}
question["name"]=input("Hello, what is your name")
question["age"]=int(input("How old are you?"))
question["colour"]=input("What is your favourite colour?")
question["python"]=input("Do you like python? Yes/no")
question["world"]=input("Is the world flat? True/False")

answers = questions(*list(question.values()))

print(" Your input was" ,question, "Thanks!")
