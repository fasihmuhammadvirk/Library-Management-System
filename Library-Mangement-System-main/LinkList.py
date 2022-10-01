#importing the filehandling file
import Filehandling as B
#import the stack and queue file
import Stack_Queue as R

#Creating the object of the stack
S = R.Stack()

#creating the object of the queue
Q = R.Queue()

#dictionaries to hold the temporary records
record_of_request = {}
record_of_issue = {}

#Creating the Node class
class NodeD:

    def __init__ (self, data):
        self.data = data
        self.previous = None
        self.next = None

#Crearing the Class For Admin fucnions using DoubleLinkList
class AdminsFunctions:

    #Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.ctr = 0

    #Creating a Link List using data in the files
    def creatinglinklist(self,Data):
        newNode = NodeD(Data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
            self.ctr = self.ctr + 1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            self.ctr = self.ctr + 1

    #Creating a function to Add a new Book in thr data base
    def InsertnewBook(self, Data):
        newNode = NodeD(Data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
            self.ctr += 1
            B.Add_Book(newNode.data)
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            self.ctr += 1
            B.Add_Book(newNode.data)

    def deletebeg(self):
        if self.head == None:
            print('''
     |---------------|
     | No Node Exist |
     |---------------|\n
                ''')
        else:
            self.head = self.head.next
            self.head.previous = None
            self.ctr -= 1
            return

    def deleteend(self):

        if self.head == None:
            print('''
     |---------------|
     | No Node Exist |
     |---------------|\n
                ''')
        elif self.ctr == 1:
            self.ctr = 0
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp = None
            self.ctr -= 1
            return

    def DeleteaBook(self,Data):

        ToDelete = NodeD(Data + "\n")
        curode = self.head
        while curode is not None:
            if ToDelete.data == curode.data:
                B.Delete_Book(Data)
                nodeToDelete = NodeD(Data + "\n")
                print(nodeToDelete.data)
                if self.head == None:
                    pass
                else:
                    index = 1
                    if nodeToDelete.data == self.head.data:
                        index = 1
                    else:
                        curNode = self.head
                        while curNode is not None:
                            if nodeToDelete.data == curNode.data:
                                break
                            else:
                                curNode = curNode.next
                                index = index + 1
                if self.head == None:
                    pass
                else:

                    if index == 1:
                        self.deletebeg()
                    elif index == self.ctr:
                        self.deleteend()
                    else:
                        temp = self.head
                        i = 1
                        while i < index:
                            temp = temp.next
                            i += 1
                        temp.previous.next = temp.next
                        temp.next.previous = temp.previous
                        temp.next = None
                        temp.previous = None
                        self.ctr -= 1
                        return
                break
            else:
                curode = curode.next



    def traverse(self):
        curnode = self.head
        if(self.head is None):
            print(
                '''
     |---------|
     | No item |
     |---------|\n
                ''')
        else:
            while (curnode is not None):
                print(curnode.data)
                curnode = curnode.next

    #Function for Searching a book in the data base
    def Search_book(self,booktosearch):

        curNode = self.head
        if (self.head == None):

            print(
                '''
     |---------------------------------|
     | This Library Has No Book: Sorry |
     |---------------------------------|\n
                ''')
            return
        while (curNode is not None):

            if curNode.next.next == None and curNode.data != booktosearch + '\n':
                print(
                    '''
     |--------------------------------------------------|
     | The Book You Looking for is not Available: Sorry |
     |--------------------------------------------------|\n
                    ''')
                break

            if curNode.data == booktosearch + '\n':
                print(
                    f'''
     |------------------------------------------------------|
     | The Book You Looking for is Available {curNode.data} |
     |------------------------------------------------------|\n
                    ''')
                break
            else:
                curNode = curNode.next

    #Function to take the input from the user
    def request_for_issue(self,userid, bookname):
        Q.enqueue(userid)
        Q.Requests()
        record_of_request[userid] = bookname
    #Function for checking the Request of the user
    def check_for_request(self):
        Q.ListofRequests()

    #Function to issue a book to user
    def issue_book(self):
        if Q.is_empty():
            print(
                '''
     |-------------------------|
     | No Request in the Queue |
     |-------------------------|\n
                ''')
        else:
            fperson = Q.deqeue()
            booktoissue = record_of_request[fperson]
            del record_of_request[fperson]
            record_of_issue[fperson] = booktoissue
            self.DeleteaBook(booktoissue)
            print(
               f'''
     |--------------------------------------------------------|
     | User {fperson} have been Issued the Book {booktoissue} |
     |--------------------------------------------------------|\n
               ''')

    #Function to reutrn the book
    def return_book(self,userid,bookname):
        S.push(bookname)
        S.push(userid)
        if userid in record_of_issue:
            booktoreturn = record_of_request[userid]
            self.InsertnewBook(booktoreturn)
            del record_of_issue[userid]
        askforreissue = input(
            '''
     |-------------------------------------------------------|
     | Do You want to Reissue the same Book Right Know?(Y/N) |
     |-------------------------------------------------------|>>'''

            )
        #for reissue the book
        if askforreissue == 'Y' or 'y':
            fperson = S.pop()
            booktoissue = S.pop()
            record_of_issue[fperson] = booktoissue
            self.DeleteaBook(booktoissue)
            print(
               f'''
     |--------------------------------------------------------------|
     | User {fperson} you have been reissued the Book {booktoissue} |
     |--------------------------------------------------------------|\n
                ''')
        else:
            while True:
                if S.isempty():
                    S.pop()
    def bookisissue(self,userid,bookname):
        val = record_of_issue.get(userid,bookname)
        if val in record_of_issue.values():
            print(
                '''
     |-----------------------|
     | Book is Issued To You |
     |-----------------------|\n
                ''')
        elif val in record_of_request:
            print(
                '''
     |-------------------------------|
     | Your Request is Still Pending |
     |-------------------------------|\n
                ''')
        else:
            print(
                '''
     |-------------------------------------|
     | You did request for a book to issue |
     |-------------------------------------|\n
                ''')

admin = AdminsFunctions()

def creatdlink():
    with open("Books.txt","r") as rd:
        Book = rd.readlines()
        for i in Book:
            admin.creatinglinklist(i)

def userfunc(choice,userid):

    if choice == '1':
        #req for issue
        bookforissue = input('''
     |----------------------------------------------------------|
     | Enter the name of the book you want to request for issue |
     |----------------------------------------------------------|>>''')
        admin.request_for_issue(userid,bookforissue)
    elif choice == '2':
        #return book
        booktoreturn = input('''
     |-----------------------------------------------|
     | Enter the name of the book you want to return |
     |-----------------------------------------------|>>''')
        admin.return_book(userid,booktoreturn)
    elif choice == '3':
        booktoview = input('''
     |---------------------------------------------|
     | Enter the name of the book you want to view |
     |---------------------------------------------|>>''')
        admin.Search_book(booktoview)
        #view book
    elif choice == '4':
        booknameis = input('''
     |------------------------------------------|
     | Enter the name of the book you issue for |
     |------------------------------------------|>>''')
        admin.bookisissue(userid,booknameis)


def AdminFunc(dec):


    if dec == '1':
        #insertbook
        booktoinsert = input(
            '''
     |-----------------------------------------------|
     | Enter the Name of the Book You want to Insert |
     |-----------------------------------------------|>>''')
        admin.InsertnewBook(booktoinsert)
    elif dec == '2':
        #del book
        booktodel = input(
            '''
     |-----------------------------------------------|
     | Enter the Name of the Book You want to Delete |
     |-----------------------------------------------|>>''')
        admin.DeleteaBook(booktodel)
    elif dec == '3':
        #view book
        booktoview = input(
            '''
     |---------------------------------------------|
     | Enter the Name of the Book You want to View |
     |---------------------------------------------|>>''')
        admin.Search_book(booktoview)

    elif dec == '4':
        #list of req
        admin.check_for_request()
    elif dec == '5':
        #issue book
        admin.issue_book()
    elif dec == '6':
        if record_of_issue == {}:
            print(
                '''
     |-----------------|
     | No Record Found |
     |-----------------|\n
                ''')
        else:
            print(record_of_issue,end = "\n" )
    else:
        print(
            '''
     |---------------|
     | Invalid Input |
     |---------------|\n
            '''
            )
creatdlink()

