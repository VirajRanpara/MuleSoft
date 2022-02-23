import sqlite3

class connect:
    def __init__(self):
        self.con = sqlite3.connect("MovieDB.db")
        self.con.execute("create table if not exists Movies(name text, actor text, actress text, director text, year_of_release int)")
    
    def insert(self,name,actor,actress,director,year_of_release):
        self.con.execute("insert into Movies(name,actor,actress,director,year_of_release) values(?,?,?,?,?)",(name,actor,actress,director,year_of_release))
        self.con.commit()
        print("====================================")
        print("Record Inserted Successfully.")
        print("====================================")

    def display(self):
        data = self.con.execute("select * from Movies")
        for row in data:
            print("====================================")
            print("Movie Name : {}".format(row[0]))
            print("Actor Name : {}".format(row[1]))
            print("Actress Name : {}".format(row[2]))
            print("Director Name : {}".format(row[3]))
            print("Year Of Release Date : {}".format(row[4]))

    def display2(self,actor,actress):
        data = self.con.execute("select name from Movies where actor=? and actress=?",(actor,actress))
        for row in data:
            print("====================================")
            print("Movie Name : {}".format(row[0]))