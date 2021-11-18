# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: November 11, 2021
# Lab Number: 8
# Program Inputs: [What information do you request from the user?]
# Program Outputs: List of names and one name picked

# Random module is imported
import random


# Function that opens the file with the names and puts them in a list.
def load_name_list(file_name):
    names_file = open(file_name, "r")
    list_of_names = []
    for line in names_file:
        list_of_names.append(line.strip())
    names_file.close()
    return list_of_names


# Function that returns one name from the list
def pop_random_name(list_of_names):
    index_value = random.randrange(len(list_of_names))
    name = list_of_names[index_value]
    list_of_names.pop(index_value)
    return name


# Function that loads the names from the file
def get_name(user_file):
    names = load_name_list(user_file)
    print(names)
    chosen_name = pop_random_name(names)
    print(chosen_name)


# Main function
def main():
    user_file = input("what is the name of your file: ")
    try:
        get_name(user_file)
    except FileNotFoundError:
        print("Sorry this file does not exist!")
        exit()
    next_choice = input("Would you like to continue? >")
    next_choice = next_choice.strip().lower()
    if next_choice == "yes":
        main()
    elif next_choice == "no":
        print("Thanks for using code!")
    else:
        next_choice = input("Would you like to continue? >")


main()
