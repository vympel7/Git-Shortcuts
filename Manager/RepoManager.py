from github import Github
from github.GithubObject import NotSet
import json, os

def list_repos(user):
    n = 0
    repos = user.get_repos()
    for repo in repos:
        print("\n({}): {}".format(n, repo.name))
        n += 1

def create_repo(user, name):
    if name != []:
        name = name[0]
    if os.path.exists(os.path.dirname(os.path.dirname(__file__)) + "\\Data\\RepoData\\CreateRepoDefaultSettings.json"):
        use_def = input("Use default settings (y/n)?\n").lower().strip()
        if use_def == "y":
            with open(os.path.dirname(os.path.dirname(__file__)) + "\\Data\\RepoData\\CreateRepoDefaultSettings.json") as f:
                home_page, priv, auoti = json.load(f).values()
            if name == []:
                name = input("Enter the new repository name: ")
            description = input("Enter the new repository description: ")
            user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)
        
    else:
        print("\nPress enter to leave the parameter blank\n")
        
        if name == []:
            name = input("Enter the new repository name: ")
        description = input("Enter the new repository description: ")
        home_page = input("Enter the new repository homepage: ")
        priv = input("Set repository to private (y/n)?\n").lower().strip()
        autoi = input("Automatically initialize the repository (y/n)?\n").lower().strip()
        
        save_repo_data([home_page, priv, autoi])
        
        user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)


def fpush(user, args):
    repos = user.get_repos()
    if len(args) == 0:
        print("Push to which repository?")
        list_repos(user)
        repo_name = input("\n").strip()
        try:
            repo = user.get_repo(repo_name)
            file_path = input(f"Insert file path to push to repository {repo_name}: ").strip()
            if os.path.exists(file_path):
                commit_message = input("Insert a commit message: ").strip()
                branch = input("Push to which branch? (leave blank for master): ").strip()
                with open(file_path) as f:
                    repo.create_file(file_path, commit_message, f.read().encode("utf-8"), branch = "master" if branch == "" else branch)
            else:
                print(f"File {file_path} was not found")
                fpush(user, args)
        except:
            print(f"Repository {repo_name} was not found")
            fpush(user, args)
    
    elif len(args) == 1:
        if ((repo_name := args[0]) in repos):
            repo = user.get_repo(repo_name)
            file_path = input(f"Insert file path to push to repository {repo_name}: ").strip()
            if os.path.exists(file_path):
                commit_message = input("Insert a commit message: ").strip()
                branch = input("Push to which branch? (leave blank for master): ").strip()
                with open(file_path) as f:
                    repo.create_file(file_path, commit_message, f.read().encode("utf-8"), branch = "master" if branch == "" else branch)
            else:
                print(f"File {file_path} was not found")
                fpush(user, args)
        else:
            print(f"Repository {repo_name} was not found")
            fpush(user, args)
    
    else:
        if ((repo_name := args[0]) in repos):
            repo = user.get_repo(repo_name)
            file_path = args[1]
            if os.path.exists(file_path):
                commit_message = input("Insert a commit message: ").strip()
                branch = input("Push to which branch? (leave blank for master): ").strip()
                with open(file_path) as f:
                    repo.create_file(file_path, commit_message, f.read().encode("utf-8"), branch = "master" if branch == "" else branch)
            else:
                print(f"File {file_path} was not found")
                fpush(user, args)
        else:
            print(f"Repository {repo_name} was not found")
            fpush(user, args)


def save_repo_data(data_list):
    save_def = input("Save settings as default for the next repositories [Repository name and description won't be saved] (y/n)?\n").lower().strip()
    
    if save_def == "y":
        data =  {
                    "home_page": data_list[0],
                    "priv": data_list[1],
                    "autoi": data_list[2]
                }
        
        try:
            os.mkdir("Data");os.chdir("Data")
            try:
                os.mkdir("RepoData")
                os.chdir(os.path.dirname(os.path.dirname(__file__)))
                with open("Data\\RepoData\\CreateRepoDefaultSettings.json", "w") as f:
                    json.dump(data, f)
            except:
                os.chdir(os.path.dirname(os.path.dirname(__file__)))
                with open("Data\\RepoData\\CreateRepoDefaultSettings.json", "w") as f:
                    json.dump(data, f)
        except:
            os.chdir("Data")
            try:
                os.mkdir("RepoData")
                os.chdir(os.path.dirname(os.path.dirname(__file__)))
                with open("Data\\RepoData\\CreateRepoDefaultSettings.json", "w") as f:
                    json.dump(data, f)
            except:
                os.chdir(os.path.dirname(os.path.dirname(__file__)))
                with open("Data\\RepoData\\CreateRepoDefaultSettings.json", "w") as f:
                    json.dump(data, f)