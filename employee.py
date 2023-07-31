import sqlite3 as db
import prospect as pt
import Admin as ad
conn=db.connect("empdb")
cur=conn.cursor()
def slfpasschg():
        #this function is used to change the password of the employees(self)
##    conn=db.connect("empdb")
##    cur=conn.cursor()
    pwd=input("enter new password\n")
    updatequery=f"update employee set userPass='{pwd}' where userName='{username}';"
    if cur.execute(updatequery):
        print("Your password changed successfully")
    conn.commit()
    cur.close()
    conn.close()

#------------------------------------others_Pass_change---------------------------------------#


def othpasschg():
        #this function is used to change the password of the other employees
##    conn=db.connect("empdb")
##    cur=conn.cursor()
    username=input("Enter the username\n")
    pwd=input("enter new password\n")
    updatequery=f"update employee set userPass='{pwd}' where userName='{username}';"
    if cur.execute(updatequery):
        print("Your password changed successfully")
    conn.commit()
    cur.close()
    conn.close()

#--------------------------------------others_Pass_change-------------------------------------#
    
#--------------------------------------Employee_login-----------------------------------------#
def login():
        #this function is used to login the employees
##    conn=db.connect("empdb")
##    cur=conn.cursor()
    while True:
        userName=input("enter your login user name please\n")
        userPass=input("enter your login Password please\n")
        selectqueryemp=f"""select userPass from employee where userName='{userName}'and userPass='{userPass}';"""
        cur.execute(selectqueryemp)
        table=cur.fetchall()
        for row in table:
            res=row[0]
            if res==userPass:
                print("successfully logged in")
                selectqueryemp=f"""select userType from employee where userName='{userName}';"""
                cur.execute(selectqueryemp)
                table2=cur.fetchall()
                for row in table2:
                    rs=row[0]
                if rs=="admin":
                    admin()
                elif rs=="monitor":
                    monitor()
                else:
                    print("error")
                break
            else:
                print("username or pass is wrong")
                break
    
    conn.commit()
    cur.close()
    conn.close()
#--------------------------------------Employee_login-----------------------------------------#
    
#--------------------------------------Monitor Panel-----------------------------------------#    
def monitor():
##    conn=db.connect("empdb")
##    cur=conn.cursor()
    
    while True:
        ch=int(input("""choose an option:
                1:Add New Prospect
                2:View All Prospect
                3:Update Prospect
                4:Search
                5:Change Password
                6:Signout\n"""))
        if ch==1:
            pt.tablecreate()
            pt.insertdata()
        elif ch==2:
            pt.disrecpros()
        elif ch==3:
            pt.updatepros()
        elif ch==4:
            pt.searchpros()
        elif ch==5:
            slfpasschg()
        elif ch==6:
            print("good bye")
            login()
        else:
            print("invalid selection, please try again")
    
    conn.commit()
    cur.close()
    conn.close()

#--------------------------------------Monitor Panel-----------------------------------------#

#--------------------------------------Admin Panel-----------------------------------------#
def admin():
##    conn=db.connect("empdb")
##    cur=conn.cursor()
    while True:
        conn=db.connect("empdb")
        cur=conn.cursor()
        ch=int(input("""choose an option:
                1:Add New Account
                2:View All Users(Employees)
                3:View All Prospects
                4:Change Password
                5:Search Prospect
                6:Activiate/Deacticate Account
                7:Signout\n"""))
        if ch==1:
            st=int(input("""Select Type of accout to create:
                    1:Monitor
                    2:Admin
                    \n"""))
            if st==1:
                typ="monitor"
                ad.createemp(typ)
            elif st==2:
                typ="admin"
                ad.createemp(typ)
                
            else:print("wrong selection")
            
            
        elif ch==2:
            ad.disrecemp()
        elif ch==3:
            pt.disrecpros()
        elif ch==4:
           st1=int(input("""Select an option:
                    1:Change own password
                    2:Change others Pass\n"""))
           if st1==1:
               slfpasschg()
           elif st1==2:
               othpasschg()
                   
        elif ch==5:
            pt.searchpros()
        elif ch==6:
            user=input("Enter the your username\n")
            st2=int(input("""Select an option:
                    1:Activate
                    2:Deactivate\n"""))
            if st2==1:
                updatequery=f"""update employee set status='{activated}' where userName='{user}';"""
            elif st2==2:
                updatequery=f"""update employee set status='{deactivated}' where userName='{user}';"""
            else:print("invalid selection,please try again")
            if cur.execute(updatequery):
                    print("successfully updated")    
        elif ch==7:
            print("good bye")
            login()
        else:
            print("invalid selection, please try again")
    
    conn.commit()
    cur.close()
    conn.close()
#--------------------------------------Admin Panel-----------------------------------------#
