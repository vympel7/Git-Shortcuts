class EditAttributes:
    print("\nPress enter to leave the attribute as it is\n")

    def name(repo):
        print(f"Current name is: {repo.name}")
        new_name = input("Insert the new name: ").strip()
        repo.edit(new_name if new_name != "" else repo.name)

    def description(repo):
        print(f"Current description is: {repo.description}")
        new_description = input("Insert the new description: ").strip()
        repo.edit(repo.name, description = new_description if new_description != "" else repo.description)

    def visibility(repo):
        private = "private" if repo.private else "public"
        print(f"Current visibility is: {private}")
        while (new_visibility := int(input("Press 0 to make this repository private and 1 to make it public: ").strip())) not in [0, 1]:
            continue
        repo.edit(repo.name, private = False if new_visibility else True)

    def website(repo):
        print(f"Current homepage link is: {repo.homepage}")
        new_homepage = input("Insert the new homepage link: ").strip()
        repo.edit(repo.name, homepage = new_homepage if new_homepage != "" else repo.homepage)

    def topics(repo):
        print("Current topics are:")
        for t in repo.get_topics():
            print(t + "\n")
        while (choice := int(input("Press 0 to add a topic and 1 to remove one: ").strip())) not in [0, 1]:
            print("\nInsert a valid number\n")
        if choice:
            topics = repo.get_topics()
            n = 0
            for topic in topics:
                print("({}): {}".format(n, topic))
                n += 1
            while (remove_topic := input("What topic do you want to remove?\n").strip()) not in topics:
                print("\nInsert a valid topic\n")
            topics.remove(remove_topic)
            repo.replace_topics(topics)
        else:
            topics = repo.get_topics()
            n = 0
            for topic in topics:
                print("({}): {}".format(n, topic))
                n += 1
            topics.append(add_topic)
            repo.replace_topics(topics)