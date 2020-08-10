from github import Github
import json, os


def login():
    if os.path.exists(os.path.dirname(__file__) + "\\Data\\AuthenticationData\\LoginDefaultSettings.json"):
        def_set_choice = input("\nDo you want to use the default login settings (y/n)?\n").lower().strip()
        if def_set_choice == "y":
            login_choice, org_or_user, token, username, password, hostname = load_data().values()
            return login_options(login_choice, org_or_user, options = [token, username, password, hostname])


    print("\nChoose how to login to your github account")
    print("(0) Token")
    print("(1) Username and password")
    print("(2) Github Enterprise with custom hostname")
    
    to_save = list(range(6))
    login_choice = get_choice(": ", [0, 1, 2])
    to_save.insert(0, login_choice)

    org_or_user = get_choice("\nYou're an organization (0) or an user (1)?\n", [0, 1])
    to_save.insert(1, org_or_user)

    return login_options(login_choice, org_or_user, to_save)
    



def login_options(login_option, org_or_user_option, save_list = None, options = None):
    if options != None:
        token, username, password, hostname = options
        if not login_option:
            return Github(login_or_token = token).get_user() if org_or_user_option else Github(login_or_token = token).get_organization()
        elif login_option == 1:
            return Github(username, password = password).get_user() if org_or_user_option else Github(username, password = password).get_organization()
        else:
            return Github(base_url = f"https://{hostname}/api/v3", login_or_token = token).get_user() if org_or_user_option else Github(base_url = f"https://{hostname}/api/v3", login_or_token = token).get_organization()
    
    if not login_option:
        token = input("\nEnter your github token: ").strip()
        save_list.append(token)
        save_data(save_list)
        return Github(login_or_token = token).get_user() if org_or_user_option else Github(login_or_token = token).get_organization()
    elif login_option == 1:
        username = input("\nEnter your github username: ").strip()
        save_list.insert(3, username)
        password = input("\nEnter your github password: ").strip()
        save_list.insert(4, password)
        save_data(save_list)
        return Github(username, password = password).get_user() if org_or_user_option else Github(username, password = password).get_organization()
    else:
        hostname = input("\nEnter your company hostname: ").strip()
        save_list.insert(5, hostname)
        save_data(save_list)
        return Github(base_url = f"https://{hostname}/api/v3", login_or_token = token).get_user() if org_or_user_option else Github(base_url = f"https://{hostname}/api/v3", login_or_token = token).get_organization()


def get_choice(lastmessage, num_range):
    check = input(lastmessage)
    
    try:
        check = int(check)
    except Exception as e:
        print("\nMust enter a valid number")
        return get_choice(lastmessage, num_range)

    if check not in num_range:
        print("\nSelected number must be between {} and {}".format(num_range[0], num_range[-1]))
        return get_choice(lastmessage, num_range)
    
    return check



def save_data(save_list):
    save_def = input("\nSave data as default for the next login sessions (y/n)?\n").lower().strip()

    data = {
               "choice": 1,
               "org_or_user": 1,
               "token": "",
               "username": "",
               "password": "",
               "hostname": ""
           }
    
    if save_def == "y":
        for i in range(len(data.values())):
            data[list(data.keys())[i]] = save_list[i]
        
        os.mkdir("Data");os.chdir("Data")
        os.mkdir("AuthenticationData")
        os.chdir(os.path.dirname(__file__))
        with open("Data\\AuthenticationData\\LoginDefaultSettings.json", "w") as f:
            json.dump(data, f)



def load_data():
    if os.path.exists(os.path.dirname(__file__) + "\\AuthenticationData\\LoginDefaultSettings.json"):
        with open("Data\\AuthenticationData\\LoginDefaultSettings.json") as f:
            return json.load(f)
    return 0