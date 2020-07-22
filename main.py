#gonna put it all in a single file for faster response

import os
import sys
import random
import time
import getpass
from time import sleep

from colorama import init
from colorama import Fore, Back, Style
init()

class colours:
	error = Style.BRIGHT + Fore.RED + "[!] " + Fore.WHITE
	warning = Style.BRIGHT + Fore.YELLOW + "[!] " + Fore.WHITE
	prompt = Style.BRIGHT + Fore.CYAN + "[enter command] " + Style.RESET_ALL
	action = Style.BRIGHT + Fore.YELLOW + "--> " + Fore.WHITE
	question = Style.BRIGHT + Fore.YELLOW + "[?] " + Fore.WHITE
	loading = Style.BRIGHT + Fore.BLUE + ":: " + Fore.WHITE


dbfper = 0
intper = 0
unlock = 0
incorrectAttempts = 0
passfile1 = open("passfile.ytr", "r")
passfile = passfile1.read()
username1 = open("username.ytr", "r")
username = username1.read()

while dbfper <= 100:
	print(colours.loading + "Loading Database Files: {dbfper}%".format(dbfper=dbfper))
	sys.stdout.write("\033[F") # Cursor up one line
	dbfper = dbfper + 6.25
	sleep(random.uniform(0.1, 0.2))

print("")

while intper <= 100:
	print(colours.loading + "Loading Initialisation Data: {intper}%".format(intper=intper))
	sys.stdout.write("\033[F") # Cursor up one line
	intper = intper + 6.25
	sleep(random.uniform(0.1, 0.2))

print("")
print(" __  ____  _") ; sleep(0.2)
print("/     |    |") ; sleep(0.2)
print("\     |    |") ; sleep(0.2)
print(" --   |    -") ; sleep(0.2)
print("") ; sleep(0.2)
print(Style.RESET_ALL)
print("© Carrot Tech Industries") ; sleep(0.2)
print("A sub division of Yetroll®\n") ; sleep(0.2)
print(colours.loading + "Loading cOS 1.3.1...") ; sleep(2)

print("User:", username)
print("")


def calculator():
	n = 0
	k = 0
	operation = 0
	while n == 0:
		k = 0
		operation = 0
		print("darrotOS calculator by Daniel071")
		input("Press enter to continue!")
		while operation == 0:
			print("Would you like for me to")
			print("Add (a)")
			print("Subtract (s)")
			print("Multiply (m)")
			inputAnswer = input("or Divide? (d)")
			if inputAnswer == "a":
				operation = "a"
			elif inputAnswer == "s":
				operation = "s"
			elif inputAnswer == "m":
				operation = "m"
			elif inputAnswer == "d":
				operation = "d"
			else:
				print("Sorry! Please use either a, s, m or d")

		firstNumber = int(input("What is your first number? "))
		secondNumber = int(input("What is your second number? "))
		if inputAnswer == "a":
			answer = firstNumber + secondNumber
		elif inputAnswer == "s":
			answer = firstNumber - secondNumber
		elif inputAnswer == "m":
			answer = firstNumber * secondNumber
		elif inputAnswer == "d":
			answer = firstNumber / secondNumber

		print("Your answer is", answer)
		while k == 0:
			inputAnswer = input("New calculation? [y / n] ")
			if inputAnswer == "n":
				n = 1
				k = 1
			elif inputAnswer == "y":
					print("Repeating")
					k = 1
			else:
				print("Please enter either [y / n]")


def main():
	sysRun = True
	while sysRun is True:
		commandInput = input(colours.prompt)
		if commandInput == "/help":
			print("Use /sysinfo to bring up information about the system!\n")

		elif commandInput == "/calculator":
			calculator()

		elif commandInput == "/exit":
			sysRun = False
			exit()


while unlock == 0:
	if passfile == "null":
		input("Press Enter")
		unlock = 1
		main()

	elif incorrectAttempts <= 5:
		passInput = getpass.getpass(colours.question + "Enter Password: ")
		if passInput == passfile:
			unlock = 1
			main()
		else:
			unlock = 0
			incorrectAttempts = incorrectAttempts + 1
			print(colours.error + "Incorrect password!\n")
	else:
		print("")
		print(colours.error + "Incorrect password inputed too many times!")
		time.sleep(0.5)
		print(colours.action + "Exiting...\n")
		time.sleep(1)
		exit()
