### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here

new_book =  {
        "title": "Divergent",
        "author": "Veronica Roth",
        "year": 2011,
        "rating": 4.2,
        "pages": 487
    }

def add_stuff(book):
    with open("library.txt", 'w') as f:
        f.write(f'{book['title']}, {book['author']}, {book['year']}, {book['rating']}, {book['pages']}\n')


add_stuff(new_book)

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


my_file("library.txt")





### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

 
if __name__ == '__main__':
    main_menu():


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

