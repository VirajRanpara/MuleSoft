from conn import *

class movies:
    def getDetails(self):
        self.name = input("Enter Movie Name : ")
        self.actor = input("Enter Actor Name : ")
        self.actress = input("Enter Actress Name : ")
        self.director = input("Enter Director Name : ")
        self.year_of_release = int(input("Enter Year Of Release : "))
    
    def insertDetails(self):
        con = connect()
        self.getDetails()
        con.insert(self.name,self.actor,self.actress,self.director,self.year_of_release)
    
    def displayDetails(self):
        con = connect()
        con.display()
    
    def displayDetails2(self):
        con = connect()
        actor = input("Enter Actor Name : ")
        actress = input("Enter Actress Name : ")
        con.display2(actor,actress)

obj = movies()

while(True):
    print("====================================")
    print("1 : Insert Data")
    print("2 : Display Data")
    print("3 : Display Data Based On Actor Name")
    print("0 : Exit")
    ch = int(input("Enter Choice : "))
    if ch == 1:
        obj.insertDetails()
    elif ch == 2:
        obj.displayDetails()
    elif ch == 3:
        obj.displayDetails2()
    elif ch == 0:
        break
    else:
        print("Invalid Choice...")