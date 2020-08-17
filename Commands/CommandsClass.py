import Authentication.Authentication as aut
import Manager.RepoManager as repom
import json

user = aut.login()

class CommandsClass:

    def commands(catcher):
        n = 0
        print("----- COMMANDS -----\n")
        with open("Commands\\Commands.json") as f:
            for command in json.load(f)["commands"]:
                print("({}): {}".format(n, command))
                n += 1

    def repos(catcher):
        print("----- REPOSITORIES -----")
        repom.list_repos(user)

    def create(name):
        repom.create_repo(user, name)

    def fpush(args):
        repom.fpush(user, args)

    def edit(args):
        repom.edit(user, args)