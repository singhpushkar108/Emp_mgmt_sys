import sqlite3 as db
import employee as emp
import os

'''
admin username= Bruce
admin pass= Ernst

monitor username= Neena
monitor pass= Devil
'''

def main():
    print("\nWelcome to Prospect Encore Analysis")
    st = "Do u Want to login"
    choice = input(st+"(Y/N):")
    if choice in ['Y','y']:
        emp.login()
    elif choice in ['N','n']:
        exit()
    else:
        print("please try again")
        main()
        
if __name__=="__main__":
    main()
