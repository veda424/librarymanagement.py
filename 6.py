
class Library:
    def __init__(self,books):
        self.books = books
    def addbooks(self,book):
        self.books.extend(book)
    def showbooks(self):
        print("Books avilable are :")
        for i,bname  in enumerate(self.books):
            print(f"SrNo {i+1}.{bname}")
        else:
            print("\n")

    def takebook(self):
        self.showbooks()
        d = int(input("Enter Sr.No a of book which you want to Buy \n"))
        delname = self.books.pop(d-1)
        print(f" You Have Taken {delname} book \n please return after reading \n Have a nice day!!! \n")

        



l = Library([])
while(True):
    un = input("what you want to perform \n 1.add Books \n 2.Show avilable Books \n 3.Take Book \n")
    if un =='q':
        break
    elif int(un) == 1:
        newbookl = list(map(str,input("enter book name to add \n").split()))
        l.addbooks(newbookl)
        print("Books added sucessfuly.... \n")
    elif int(un)==2:
        l.showbooks()
    elif int(un) ==3:
        l.takebook()
    else:
        print("invalid number")








