def main():
    name_and_email = {}
    email = str(input("Email: "))
    name = email.split("@")[0]

    while email != '':
        # get name
        part1 = email.split("@")[0]
        part2 = part1.split(".")
        name = " ".join(part2).title()

        # check did we get right name
        check = str(input("Is you name {} ?(Y/n)".format(name)).lower())
        if check != 'y' and check != '': # if yes, just press enter
            name = str(input("Name: "))
        name_and_email[name] = email
        email = str(input("Email: "))

    for name,email in name_and_email.items():
        print("{} ({})".format(name,email))


main()