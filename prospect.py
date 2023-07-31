import sqlite3 as db
import employee as emp
def tablecreate():
        #this function creates table
    conn=db.connect("prospdb")
    cur=conn.cursor()
    createquery="""create table if not exists prospects(
    prospId int(5) primary key,
    prospName varchar(45),
    prospPhone int(12),
    prospAddress varchar(45),
    interestedModel varchar(45),
    interestedColor varchar(45),
    dateOfVisit date,
    priority varchar(45));
    """
    if cur.execute(createquery):
        print("Table Created Successfully")
    conn.commit()
    cur.close()
    conn.close()
def insertdata():
        #this inserts prospects data into database
    conn=db.connect("prospdb")
    cur=conn.cursor()
    while True:
        print("Create new prospect")
        prospId=input("Enter Id")
        prospName=input("Enter Name")
        prospPhone=int(input("Enter phone number"))
        prospAddress=input("Enter Address of prospect")
        interestedModel=input("Enter the Model prospect interested in")
        interestedColor=input("Enter the color prospect interested in")
        dateOfVisit=input("Enter the Date of Visit")
        while True:
            p=int(input("""select the priority of the prospect:
                                    1:Low
                                    2:Medium
                                    3:High
                                    """))
            if p==1:
                priority="Low"
                break
            elif p==2:
                priority="Medium"
                break
            elif p==3:
                priority="High"
                break
            else:print("""invalid selection
                        please select again""")
        insertquery=f"""insert into prospects values
                    ('{prospId}','{prospName}',{prospPhone},'{prospAddress}',
                    '{interestedModel}','{interestedColor}',
                    {dateOfVisit},'{priority}');"""

        if cur.execute(insertquery):
            print("Record inserted successfully")
        else:
            print("Some error occured please try again")
    conn.commit()
    cur.close()
    conn.close()
def disrecpros():
        #this function displays records of all prospects 
    conn=db.connect("prospdb")
    cur=conn.cursor()
    selectquery="select * from prospects;"
    
    cur.execute(selectquery)
    table=cur.fetchall()
    for row in table:
        for col in row:
            print(col,end="\t")
        print()
    conn.commit()
    cur.close()
    conn.close()
def searchpros():
            #this function displays the record of a specific prospect
    conn=db.connect("prospdb")
    cur=conn.cursor()
    while True:
        a=int(input("""Selet a searching option:
                    1:By priority
                    2:By prospect id
                    3:Main menu\n"""))
        if a==1:
            while (True):
                p=int(input("""select the priority: 
                                        1:Low
                                        2:Medium
                                        3:High
                                        \n"""))
                if p==1:
                    priority="Low"
                    break
                elif p==2:
                    priority="Medium"
                    break
                elif p==3:
                    priority="High"
                    break
                else:print("""invalid selection
                            please select again""")
            selectquery2=f"select * from prospects where priority='{priority}';"
            cur.execute(selectquery2)
            table=cur.fetchall()
            for row in table:
                for col in row:
                    print(col,end="\t")
                print()
            
        elif a==2:
            print("you chose for search by Prospect id")
            pid=input("enter the prospect id\n")
            selectquery3=f"select * from prospects where prospId={pid};"
            cur.execute(selectquery3)
            table=cur.fetchall()
            for row in table:
                    for col in row:
                        print(col,end="\t")
                    print()
        elif a==3:
            emp.login()
        else:
            print("invalid selection Please try again")
    conn.commit()
    cur.close()
    conn.close()

def updatepros():
        #this updates the data of propects
    conn=db.connect("prospdb")
    cur=conn.cursor()
    while True:
        a=int(input("""select an option to update
                        1:Phone
                        2:Model
                        3:Color
                        4:Priority
                        5:Main menu\n"""))
        if a==1:
            pid=int(input("enter prospect's id\n"))
            phone=int(input("enter the phone no.\n"))
            updatequery=f"""update prospects set prospPhone={phone} where prospId={pid};"""
            if cur.execute(updatequery):
                      print("successfully updated")
        elif a==2:
            pid=int(input("enter prospect's id\n"))
            model=input("enter the model\n")
            updatequery=f"""update prospects set interestedModel='{model}' where prospId={pid};"""
            if cur.execute(updatequery):
                      print("successfully updated")
        elif a==3:
            pid=int(input("enter prospect's id\n"))
            color=input("enter the color\n")
            updatequery=f"""update prospects set interestedColor='{color}' where prospId={pid};"""
            if cur.execute(updatequery):
                      print("successfully updated")
        elif a==4:
            pid=int(input("enter prospect's id\n"))
            while (True):
                p=int(input("""select the priority: 
                                        1:Low
                                        2:Medium
                                        3:High
                                        """))
                if p==1:
                    pri="Low"
                    break
                elif p==2:
                    pri="Medium"
                    break
                elif p==3:
                    pri="High"
                    break
                else:print("""invalid selection
                            please select again""")
            
            updatequery=f"""update prospects set priority='{pri}' where prospId={pid};"""
            if cur.execute(updatequery):
                      print("successfully updated")
        elif a==5:
            break      
    conn.commit()
    cur.close()
    conn.close()
    
