from Methods import *
from Objects import *


def run_program():
    while True:
        print("please choose one of the following options -> 1) add link, 2) find link, 3) stop")
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            full_link = input("Enter the full link: ")
            short_link = input("Enter the short link: ")

            add_link(link_service, short_link, full_link)

            print("you saved  link")

        elif user_choice == "2":
            short_link = input("Enter the short link: ")

            result = find_link(link_service, short_link)

            if result is not None:
                print("This is your link:", result)
            else:
                print("You dont have this link")

        elif user_choice == "3":
            print("program was stopped")
            break

        else:
            print("Enter valid input")