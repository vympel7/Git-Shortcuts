import sys
sys.path.append("C:\\Users\\PC_HOME\\Desktop\\Python\\github_venv\\Lib\\site-packages")
from Commands.CommandsClass import CommandsClass as cc
import json

print("\nPress q to exit!")

with open("Commands\\Commands.json") as f:
    commands = json.load(f)["commands"]

while 1:
    print("\nEnter a command: \n")
    
    command = input().lower().strip().split(" ")


    if command[0] == "q":
        break
    
    if command[0] in commands:
        getattr(cc, command[0])(command[1:])