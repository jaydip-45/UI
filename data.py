#import sqlite3 Database
import sqlite3

#create or connect with database
conn=sqlite3.connect('moviedetail.db')
print("Database created or connected....")

#Creating a Tbale
conn.execute("create table Movies(id int primary key not null,name text,actor text,actress text,director text, yearOfrelease text)")
print("Table created....")

#inserting a record into Table 
conn.execute("insert into Movies values(1,'Shershaah','Sidharth Malhotra','Kiara Advani','Vishnuvardhan',2020)")
conn.execute("insert into Movies values(2,'Om Shantim Om','Sarukh khan','Deepika Padukon','Gauri Khan',2007)")
conn.execute("insert into Movies values(3,'kabir singh','sahid Kapoor','Kiara Advani','Sandeep redy vanga',2019)")
conn.execute("insert into Movies values(4,'M.S.Dhoni The Untold Story','Susant singh rajput','Disha patni','Neeraj panday',2016)") 
conn.commit()

#fetch the record from Table
data=conn.execute("select * from Movies")

for row in data:
    print("id:",row[0])
    print("Name:",row[1])
    print("Actor:",row[2])
    print("Actress:",row[3])
    print("Director:",row[4])
    print("Year Of Release:",row[5])

    print("-----------------------------")
    

#fetch actress and acor name with particular movie name
data1=conn.execute("select actress,actor  from Movies where name='Shershaah'")

for row1 in data1:
    print(row1)
