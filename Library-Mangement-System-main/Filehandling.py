#Function to add the book into the file
def Add_Book(val):
    with open("Books.txt","a") as a:
        a.write(val.strip('\n'))
        print(f'''
        |---------------------|
        | {val} Book is Added |
        |---------------------|\n
''')
    a.close()

#function to delete the book from the file
def Delete_Book(booktodel):
    with open("Books.txt", "r") as f:
        Books = f.readlines()

    with open("Books.txt", "w") as f:
        for Book in Books:
            if Book == None:
                print('''
     |----------------------|
     | The Library is Empty |
     |----------------------|\n
                      ''')
                break
            else:
                if Book.strip("\n") is not booktodel:
                    if Book == booktodel+'\n':
                        print(f'''
     |------------------------------|
     | {booktodel} Book is Deleted  |
     |------------------------------|\n
                               ''')
                    else:
                        f.write(Book)
    f.close()

#function to return a certain book from the files
def issue_book(bookname):
    with open("Books.txt", "r") as f:
        Book = f.readlines()
        for i in Book:
            if i == bookname:
                return i

#function to check if a book is avaliable in the data base or not
def view_book(bookname):
    with open("Books.txt", "r") as f:
        Book = f.readlines()
        for i in Book:
            if i == bookname:
                print(
                    '''
     |----------------------------|
     | Yes The Book Is Available  |
     |----------------------------|\n
                    ''')
