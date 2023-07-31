import sqlite3 as db

conn=db.connect("empdb")
cur=conn.cursor()
def createemp(usertype):
        #this creates employee table and/or insert data
    createqry="""create table if not exists employee
                (  userName varchar(45) primary key,
                   userPass text,
                   userType text,
                   fullName text,
                   phone int(12),
                   email text,
                   status text
                );"""
    if cur.execute(createqry):
        print("success table")
    userName=input("enter username\n")
    userPass=input("create password\n")
    userType=usertype
    fullName=input("enter full name")
    phone=int(input("enter the phone no."))
    email=input("enter the email")
    while True:
        s=int(input(f"""select the stsatus of the employee
                        1:Activated
                        2:Deactivated\n
                        """))
        if s==1:
            status="activated"
            break
        elif s==2:
            status="deactivated"
            break
        else:print("""invalid selection
                     please select again""")
    insertqry=f"""insert into employee values('{userName}','{userPass}',
                '{userType}','{fullName}','{email}',{phone},'{status}')"""
    
    if cur.execute(insertqry):
        print("success")

    qry="select * from employee;"
    cur.execute(qry) 
    table=cur.fetchall()
    for row in table:
        for col in row:
            print(col,end="\t")
        print()
    conn.commit()
    cur.close()
    conn.close()

def disrecemp():
    selectquery="select * from employee;"
    cur.execute(selectquery)
    table=cur.fetchall()
    for row in table:
        for col in row:
            print(col,end="\t")
        print()
    conn.commit()
    cur.close()
    conn.close()
