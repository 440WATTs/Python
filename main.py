# This program prints Hello, world!

print('Hello, world!')
print('aditya raghunath singh',17)
print('''Ringa-ringa roses,
A pocketful of posies.
A-tishoo! A-tishoo!
We all fall down!''')

import pyttsx3
engine = pyttsx3.init()
engine.say("here i instaled a external module through a website using pip command")
engine.runAndWait()

import os

def list_directory_contents(path):
    try:
        # Check if the path is a valid directory
        if not os.path.isdir(path):
            print(f"'{path}' is not a valid directory.")
            return

        # List the contents of the directory
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # You can change this to any directory path you want to list
    directory_path = "."
    list_directory_contents(directory_path)


