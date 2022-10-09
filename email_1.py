#modules to use for application
from calendar import month
from cmath import nan
from datetime import datetime
from datetime import date
import pandas as pd
import numpy as np


#work = pd.read_excel("STUDENTS_spreadsheet.xlsx") 
work = pd.read_excel("STUDENTS_spreadsheet.xlsx", usecols=['ID', 'First Name', 'Email Address', 
    'START DATE', 'Org.', 'Gender', 'END DATE','stu_status','Exit questionnaire sent','Exit questionnarie received', 
    'Folllow up Progression in work'])


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
    blank = 1
    #print(work.loc[work['stu_status',"Exit questionnarie received"])
    #futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver") & (work['Exit questionnarie received']=="")]#.isnull())]
    #futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver") & (work['Exit questionnarie received'].isnull())]
    futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver") & (work['Exit questionnarie received']== blank)]
    #futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver")] #& (work['Exit questionnarie received'].isnull())]
    #futs= work.loc[(work["stu_status"]=="Completer") | (work["stu_status"]=="early Leaver")] #& (work['Exit questionnarie received']=="NaN")]


    print(futs)
    futs.to_csv('file_name.csv')    
    
    
    
    today = date.today() #gets todays date
    #print(today)

def work_pro():
    #work progress
    getMonth()

    studoption = int(input("Select a option:\n\n1.Work Progression men\n2.Work Progression female\n3.Exit Questionnaire\n4.Quit'\n"))

    if studoption ==1:
        futsfwp= work.loc[(work["stu_status"]=="Completer") & (work["Gender"]=="male") & (work['Folllow up Progression in work']==month1)]
        print (futsfwp)

    elif studoption == 2:
        fusfwp= work.loc[(work["stu_status"]=="Completer") & (work["Gender"]=="female") & (work['Folllow up Progression in work']=="due in september")]
        print(fusfwp)
    elif studoption == 3:
        exit_quest()
    elif studoption == 4:
        quit()
    else:
        print("Sorry do not understand\n")
        work_pro()


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()