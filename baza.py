import sqlite3

class Baza:
    def __init__(self):
        self.conn = sqlite3.connect('baza.db')
        self.cursor = self.conn.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute("create table if not exists Notes(id INTEGER not null primary key autoincrement, note varchar(100) not null,desc varchar(200),date Date)")
        self.conn.commit()


    def insertDB(self,vnote,vdesc,vdate):

        self.cursor.execute("insert into Notes(note,desc,date) values('%s','%s','%s')" % (vnote,vdesc,vdate))
        self.conn.commit()


    def outdata(self):
        data = self.cursor.execute("select * from Notes").fetchall()
        self.conn.commit()
        return data


