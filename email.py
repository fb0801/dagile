#modules to use for application
from calendar import month
from datetime import datetime
import pandas as pd

def getMonth():
    #function to get current month
    global month1
    
    today = datetime.now()
    month1 = today.strftime("%b")
    print("Current Month Full Name:", month1)


def main():
    getMonth()
    '''usecols=['ID', 'First Name', 'Last Name', 'Email Address', 
    'START DATE', 'Org.', 'Gender', 'END DATE','Completer/Early Leaver', 'Folllow up Progression in work '])'''
    
    work = pd.read_excel("spreadsheet.xlsx", usecols=['ID', 'First Name', 'Email Address', 
    'START DATE', 'Org.', 'Gender', 'END DATE', 'Exit questionnaire sent','Exit questionnarie received', 
    'Folllow up Progression in work'])
    print(work)

    work[''].where(work[''] =="")
        





def SendEmail():
    #function to send emails
    pass

def exit_quest():
    #exit questionnaire
    pass


def work_pro():
    #work progress
    pass


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()