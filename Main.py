import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "\\Lib\\site-packages")
from Commands.CommandsClass import CommandsClass as cc
import json

print("\nPress q to exit!")

with open("Commands\\Commands.json") as f:
    commands = json.load(f)["commands"]

while 1:
    print("\nEnter a command: \n")

    command = input().strip().split(" ")


    if command[0].lower() == "q":
        break

    if command[0].lower() in commands:
        getattr(cc, command[0].lower())(command[1:])