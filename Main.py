from CommandsClass import CommandsClass as cc
import json

print("\nPress q to exit!")

with open("Commands.json") as f:
    commands = json.load(f)["commands"]

while 1:    
    print("\nEnter a command: \n")
    
    command = input().lower().strip()

    if command == "q":
        break
    
    if command in commands:
        getattr(cc, command)()