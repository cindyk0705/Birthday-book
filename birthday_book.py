# Cindy Kuang 
# Homework 9 
# April 8, 2024
# This program logs birthdays and allows user to make changes to the log. 
# Input: user commands 
# Output: command-specific responses.

import os

# Here's one function for you. No reason for everyone to write this one.
def print_help(): 
    """This function can be used to print out the help message."""
    print("Allowed commands:")
    print("add firstName lastName month day year")
    print("list") 
    print("delete number")
    print("search name")
    print("save filename")
    print("load filename")
    print("help")
    print("echo on")
    print("echo off")


def main():
    """The main function of the Birthday Book program."""
    print("Welcome to the Birthday Book Manager")
    echo = False 
    book = BookList() 
    while True: 
        user_input = input(">")
        arguments = user_input.split()
        command = arguments[0]
        if echo == True: 
            print(f'You entered: \"{user_input}\"')
        if command == "add":
            add_entry(arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], book)
        elif command == 'list':
            list_entries(book)
        elif command == "search":
            search_entry(arguments[1], arguments[2], book)
        elif command == "delete":
            delete_entry(arguments[1], book)
        elif command == "echo":
            if arguments[1] == "on":
                echo = True 
            elif arguments[1] == "off":
                echo = False 
            else: 
                command_error()
        elif command == "save":
            save_file(arguments[1], book)
        elif command == "load":
            load_file(arguments[1], book)
        elif command == "help":
            print_help()
        else: 
            command_error()

class BookList():
    def __init__(self): 
        self.entries = list()
    def append(self, input):
        self.append(input)

def add_entry(firstName, lastName, day, month, year, book):
    try:
        date = CreateDate(day, month, year)
        bd = CreateBirthday(firstName, lastName, date)
        book.entries.append(bd)
        formatted_bd = format_date(bd)
        print(f'Added {formatted_bd} to birthday book.')
    except ValueError:
        print("Error: Unable to add birthday to book. Please use integers for dates.")

def format_date(bd):
    return bd.firstName + ' ' + bd.lastName + ' ' + str(bd.date.day) + '/' + str(bd.date.month) + '/' + str(bd.date.year)


class CreateDate():
    def __init__(self, day, month, year):
        self.day = day 
        self.month = month
        self.year = year 

class CreateBirthday():
    def __init__(self, firstName, lastName, date):
        self.firstName = firstName
        self.lastName = lastName
        self.date = date

def list_entries(book):
    for i in range(len(book.entries)):
        formatted_bd = format_date(book.entries[i])
        print(f'{i + 1}: {formatted_bd}')

def delete_entry(index, book):
    formatted_date = format_date(book.entries[int(index) - 1])
    response = input(f'Are you sure you want to delete {formatted_date}?')
    if response == 'y':
        book.entries.pop(index - 1)
    elif response == 'n':
        return 
    else:
        command_error()

def search_entry(lastName, firstName, book):
    index = book.entries.firstName.index


def save_file(book, filename):
    try:
        infile = (filename + '.txt', 'w')
        for i in range(len(book.entries)):
            formatted_bd = format_date(book.entries[i])
            infile.write(formatted_bd)
        infile.close() 
    except FileNotFoundError: 
        print(f'I\'m sorry, but {filename}.txt does not exist.')

def load_file(book, filename):
    try: 
        infile = (filename + '.txt', 'r')
        line = infile.readline()
        while line != '':
            arguments = line.strip()
            add_entry(arguments[1], arguments[2], arguments[3], arguments[4], arguments[5], book)
            line = infile.readline()
        infile.close()
    except FileNotFoundError:
        print(f'I\'m sorry, but {filename}.txt does not exist.')

def command_error():
    print("I am sorry, but that is not a recognized command, or")
    print("you have entered an incorrect number of arguments.")
    print("You may enter 'help' to see a list of commands.")


# Do not modify the code below.  Write all of your code above.
if __name__ == "__main__":
    main()