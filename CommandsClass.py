import Authentication as aut
import RepoManager as repom
import json

user = aut.login()

class CommandsClass:
    
    def list_commands():
        n = 0
        print("----- COMMANDS -----\n")
        with open("Commands.json") as f:
            for command in json.load(f)["commands"]:
                print("({}): {}".format(n, command))
                n += 1

    def list_repos():
        print("----- REPOSITORIES -----")
        repom.list_repos(user)
    
    def create_repo():
        repom.create_repo(user)