from github import Github
from github.GithubObject import NotSet
import json, os

def list_repos(user):
    n = 0
    repos = user.get_repos()
    for repo in repos:
        print("\n({}): {}".format(n, repo.name))
        n += 1

def create_repo(user):
    if os.path.exists(os.path.dirname(__file__) + "\\Data\\CreateRepoDefaultSettings.json"):
        use_def = input("Use default settings (y/n)?\n").lower().strip()
        if use_def == "y":
            with open("Data\\CreateRepoDefaultSettings.json") as f:
                description, home_page, priv, auoti = json.load(f).values()
            user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)
        
    else:
        print("\nPress enter to leave the parameter blank\n")
        
        name = input("Enter the new repository name: ")
        description = input("Enter the new repository description: ")
        home_page = input("Enter the new repository homepage: ")
        priv = input("Set repository to private (y/n)?\n").lower().strip()
        autoi = input("Automatically initialize the repository (y/n)?\n").lower().strip()
        
        save_data([description, home_page, priv, autoi])
        
        user.create_repo(name, description = description if description.strip() != "" else NotSet, homepage = home_page if home_page.strip() != "" else NotSet, private = True if priv == "y" else False, auto_init = True if autoi == "y" else False)


def save_data(data_list):
    save_def = input("Save settings as default for the next repositories [Repository name won't be saved] (y/n)?\n").lower().strip()
    
    if save_def == "y":
        data =  {
                    "description": data_list[0],
                    "home_page": data_list[1],
                    "priv": data_list[2],
                    "autoi": data_list[3]
                }
        
        try:
            os.mkdir("Data")
            with open("Data\\CreateRepoDefaultSettings.json", "w") as f:
                json.dump(data, f)
            return
        
        except OSError:
            with open("Data\\CreateRepoDefaultSettings.json", "w") as f:
                json.dump(data, f)
            return