# This function reads the contents of a file and returns it a string
def readFile(fileNameRead):
    # opens the file in 'read' mode with utf-8 encoding to handle all types of text; avoids previous issues I was having
    with open(fileNameRead, 'r', encoding='utf-8') as file: 
        # reads the entire content of the file and stores it in the variable called 'data'
        data = file.read()
        # returns the contents of the file that was read from it 
        return data

# This function that adds a new entry (thought) to the file
def addEntry(fileNameWrite, entry):
    # opens the file in 'append' mode with utf-8 encoding so that new content is added to the end of the file without deleting anything
    with open(fileNameWrite, 'a', encoding='utf-8') as file:
        # writes the new entry followed by a newline character, so that it appears on a new line in the file
        file.write(entry + "\n")

# the part of the main program, where the user can choose to add an entry or view existing ones 
# the program runs in a loop so the user can keep choosing what they want to do
while True: 
    # name of the file where the entries are being stored 
    theFileName = "DisneyFiles.txt"

    # prints out menu options for the user to choose from 
    print("1. Add your own thoughts to this article")
    print("2. View your added entry")
    print("3. Exit")
    
    # asks the user to enter their choice, which is saved as 'choice' 
    choice = input("Enter your choice (1/2/3): ")
    
    # if the user selects option 1, it adds an entry 
    if choice == "1":
        # get the user's input for the new journal entry
        new_entry = input("Enter your thoughts: ")
        # this calls the addEntry function to add the new entry to the file 
        addEntry(theFileName, new_entry)
        # Notifies the user that their entry has been added successfully 
        print("Your entry has been added!")
    
    # if the user selects option 2, it allows them to view the added entries 
    elif choice == "2":
        # prints a message stating what the user is about to see 
        print("You've added this feedback: ")
        # Calls the readFile function to read and display the contents of the file 
        print(readFile(theFileName))
    
    # if the user selects option 3, it exits the program 
    elif choice == "3":
        # prints a farewell message to the user 
        print("Thank you for joining me in Disney Princess nostalgia!")
        # breaks out of the loop to end the program
        break
    
    # if the user enters anything other than 1, 2, or 3
    else: 
        # prints an error message telling them to enter a valid option 
        print("Invalid choice. Please enter 1, 2, or 3.")






