from github import Github
from github.GithubObject import NotSet
import json, os

def list_repos(user):
    n = 0
    repos = user.get_repos()
    for repo in repos:
        print("\n({}): {}".format(n, repo.name))
        n += 1

def create_repo(user, name=None):
    if name != None:
        name = name[0]
    if os.path.exists(os.path.dirname(__file__) + "\\Data\\RepoData\\CreateRepoDefaultSettings.json"):
        use_def = input("Use default settings (y/n)?\n").lower().strip()
        if use_def == "y":
            with open("Data\\RepoData\\CreateRepoDefaultSettings.json") as f:
                home_page, priv, auoti = json.load(f).values()
            if name == None:
                name = input("Enter the new repository name: ")
            description = input("Enter the new repository description: ")
            user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)
        
    else:
        print("\nPress enter to leave the parameter blank\n")
        
        if name == None:
            name = input("Enter the new repository name: ")
        description = input("Enter the new repository description: ")
        home_page = input("Enter the new repository homepage: ")
        priv = input("Set repository to private (y/n)?\n").lower().strip()
        autoi = input("Automatically initialize the repository (y/n)?\n").lower().strip()
        
        save_data([home_page, priv, autoi])
        
        user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)


def save_data(data_list):
    save_def = input("Save settings as default for the next repositories [Repository name and description won't be saved] (y/n)?\n").lower().strip()
    
    if save_def == "y":
        data =  {
                    "home_page": data_list[0],
                    "priv": data_list[1],
                    "autoi": data_list[2]
                }
        
        os.mkdir("Data");os.chdir("Data")
        os.mkdir("RepoData")
        os.chdir(os.path.dirname(__file__))
        with open("Data\\RepoData\\CreateRepoDefaultSettings.json", "w") as f:
            json.dump(data, f)