#modules to use for application
from calendar import month
from datetime import datetime
from datetime import date
import pandas as pd


work = pd.read_excel("STUDENTS_spreadsheet.xlsx") 


def getMonth():
    #function to get current month
    global month1
    
    today = datetime.now()
    month1 = today.strftime("%b")
    print("Current Month Full Name:", month1)


def main():
    studentoption = int(input("Select a option:\n\n1.Exit Questionnaire to send\n2.Work Progression\n3.Quit\n'"))
    if studentoption ==1:
        exit_quest()
    elif studentoption == 2:
        work_pro()
    elif studentoption == 3:
        quit()
    else:
        print("Sorry do not understand\n")
        main()


def SendEmail():
    #function to send emails
    pass

def exit_quest():
    #exit questionnaire   

    #print(work.loc[work['stu_status',"Exit questionnarie received"])
    futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver") & (work['Exit questionnarie received'].isnull())]
    print(futs)    
    
    
    today = date.today()
    print(today)

def work_pro():
    #work progress
    getMonth()


    futsfwp= work.loc[(work["stu_status"]=="Completer")  (work["Gender"]=="male") & (work['Folllow up Progression in work']==month1)]
    
    fusfwp= work.loc[(work["stu_status"]=="Completer")  (work["Gender"]=="female") & (work['Folllow up Progression in work']==month1)]


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()