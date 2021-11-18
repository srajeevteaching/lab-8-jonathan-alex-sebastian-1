# Programmers: Jonathan, Alex, Sebastian
# Course: CS151, Dr. Rajeev
# Date: November 11, 2021
# Lab Number: 8
# Program Inputs: [What information do you request from the user?]
# Program Outputs:

def load_name_list(file_name):
    names_file = open(file_name, "r")
    list_of_names = []
    for line in names_file:
        list_of_names.append(line.strip())
    names_file.close()
    return list_of_names


names = load_name_list("names.txt")
print(names)
