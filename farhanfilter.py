'''application to fix the file 
part of https://github.com/fb0801/dagile created by Farhan Bhatti

Remove the square brackets and quotation marks from the ‘groups’ column
search for [ , replace all’. Repeat for ] and “:

'''

#application modules
import pandas as pd
import numpy as np
import os

rmv =['A','B','T','U']
rmvList =["[',']','"','"',"]

#work = pd.read_excel("STUDENTS_test.xlsx")
work =pd.read_csv("Dagile Users.csv")



def main_2():
    #data_top = work.head() #print column titles 
    #print(data_top) 
    #newfile = work.drop(columns=['A','B','T','U'] axis=1)#drop column
    newfile = work.drop(columns=['User Status', 'Tutor','Date imported','Notes'])
    #newfile = work.drop(['A','B','T','U'], axis=1)
    ##newfile = work.pop(rmv)  
    #rep= work.loc[:,"groups"]
    ##work['groups'] = work['groups'].str.replace("['", )
    ##work['groups'] = work['groups'].str.replace("']", )
    
    
    ###newfile['groups'] = newfile['groups'].str.replace('\W', '', regex=True)
    newfile['groups'] =newfile['groups'].str.replace('[', '')
    newfile['groups'] =newfile['groups'].str.replace(']', '')
    newfile['groups'] =newfile['groups'].str.replace('"', '')
   
    name = input("Enter name of file: ")
    
    dagile = newfile.to_csv(f'{name}.csv')
   
    newDagile = dagile
    print(newDagile)

    print("task completed")



if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main_2()