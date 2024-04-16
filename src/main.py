from random import randint
from sys import platform
from os import getcwd, system, getlogin # Get current directory
from platform import node # Get machine name
from colorama import init, Fore
from sys import exit # For compiling (because typing exit() doesnt work in compiled versions)

init(autoreset=True)
username = getlogin()
machine_name = node()

def GetDirectory():
	if platform == "win32": # Windows based OS
		directory = getcwd()
	else: # Unix based OS
		directory = getcwd().replace(f"/home/{username}", "~")
	
	return directory

def GetCommand(directory, username, machine_name):
	if platform == "win32": # Windows based OS
		command = input(directory+">")
	else: # Unix based OS
		command = input(Fore.LIGHTGREEN_EX + f"{username}@{machine_name}" + Fore.RESET + ":" + Fore.LIGHTBLUE_EX + directory + Fore.RESET + "$ ")

	return command

if __name__ == "__main__":
	while True:
		directory = GetDirectory()
		command = GetCommand(directory, username, machine_name)

		num = randint(1, 2)

		if num ==1 and command == "exit":
			exit()
		elif num == 1:
			system(command)
		else:
			print("Nah I don't feel like it.")
else:
	pass
