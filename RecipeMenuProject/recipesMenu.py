import os
from pathlib import Path
from os import system




start_location = input("Please insert the project location folder, separated by backspace")
locationPathList = start_location.split(' ')

##CHANGE to \ if using WINDOWS
locationPath = "/".join(locationPathList)

folder_location = Path(Path.home(), locationPath)


def folder_count(folder_name):
    count = 0
    for txt in Path(folder_name).glob('**/*.txt'):
        count += 1
    return count

def getContent (file_name, location):
    if file_name != "invalid":
        print(file_name)
        new_file = open(location / file_name, 'w')
        typed_content = input("Type the recipe here")
        new_file.write(typed_content)

def welcome_section():
    print("####### Welcome #########")
    print(f'All the recipes are in {folder_location}')
    print(f'There are {folder_count(folder_location)} Recipes')
    print('#' * 50)

def readFile():
    entries = os.listdir(folder_location)
    count = 0
    for entry in entries:
        print("[" + str(count) + "] " + entry)
        count += 1

    choice_readFile = input("From which folder do you want to read from?")
    choice_readFileNumber = int(choice_readFile)

    if choice_readFileNumber <= count:
        print("You chose the folder " + entries[choice_readFileNumber] + ". Here are its files")
        new_f_location = folder_location / entries[choice_readFileNumber]
        print(new_f_location)
        f_entries = os.listdir(new_f_location)
        print('Choose which file do you want to read from:')
        count = 1
        for f_entry in f_entries:
            print("[" + str(count) + "] " + f_entry)
            count += 1
        readChoice = input()
        readChoiceInt = int(readChoice) - 1
        recipe_file = open(new_f_location / f_entries[readChoiceInt])
        print("**RECIPE**")
        print(recipe_file.read())
    selection_section()


def writeFile():
    entries = os.listdir(folder_location)
    count = 0
    print("********Choose the folder you want to insert your new recipe**********")
    for entry in entries:
        print("[" + str(count) + "] " + entry)
        count += 1
    choice_writeFile = input()
    choice_writeFileNumber = int(choice_writeFile)

    if choice_writeFileNumber <= count:
        print("****You chose the folder " + entries[choice_writeFileNumber])
        new_f_location = folder_location / entries[choice_writeFileNumber]
        file_name = input("Enter new file name")
        new_file_name = file_name + '.txt'
        f_entries = os.listdir(new_f_location)
        check = 0
        for entry in f_entries:
            if entry == new_file_name:
                print("!!!!!!This file is already in use!!!!!")
                new_file_name = "invalid"
                writeFile()
                break
            else:
                continue
        getContent(new_file_name, new_f_location)
    selection_section()




def createFolder():
    cc = input("Write down the name of the new category")
    path = Path(Path.home(), 'Desktop', 'python16Course', 'Recipes', cc)
    os.makedirs(path)
    selection_section()
def deleteFile():
    entries = os.listdir(folder_location)
    count = 0
    for entry in entries:
        print("[" + str(count) + "] " + entry)
        count += 1

    choice_deleteFile = input("From which folder you want to delete?")
    choice_deleteFileNumber = int(choice_deleteFile)

    if choice_deleteFileNumber <= count:
        print("You choose the folder:" + entries[choice_deleteFileNumber] + " Here are its files")
        new_f_location = folder_location / entries[choice_deleteFileNumber]
        print(new_f_location)
        f_entries = os.listdir(new_f_location)
        print('Choose which file do you want to delete:')
        count = 1
        for f_entry in f_entries:
            print("[" + str(count) + "] " + f_entry)
            count += 1
        deleteChoice = input()
        deleteChoiceInt = int(deleteChoice) - 1
        print(f_entries[deleteChoiceInt])
        os.remove(new_f_location / f_entries[deleteChoiceInt])

        selection_section()

def deleteFolder():
    entries = os.listdir(folder_location)
    count = 0
    for entry in entries:
        print("[" + str(count) + "] " + entry)
        count += 1

    choice_deleteFile = input("What folder you want to delete?")
    choice_deleteFileNumber = int(choice_deleteFile)

    if choice_deleteFileNumber <= count:
        new_f_location = folder_location / entries[choice_deleteFileNumber]
        os.rmdir(new_f_location)
    selection_section()







def selection_section():
    print('#' * 50)
    choice = input("Please choose one of these options\n[1]read recipe\n[2]create recipe\n[3]create category\n["
                   "4]delete recipe\n[5]delete category\n[6]end program")
    if choice == '1':
       readFile()
    if choice == '2':
        writeFile()
    if choice == '3':
        createFolder()
    if choice == '4':
        deleteFile()
    if choice == '5':
        deleteFolder()
    if choice == '6':
        end_program = True
    else:
        pass






##this is the actual menu of the program
end_program = False
while not end_program:
    welcome_section()
    selection_section()
    end_program = True
