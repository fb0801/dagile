'''application to fix the file 
part of https://github.com/fb0801/dagile created by Farhan Bhatti

Remove the square brackets and quotation marks from the ‘groups’ column
search for [ , replace all’. Repeat for ] and “:

'''

#application modules
import pandas as pd
import numpy as np

rmv =['A','B','T','U']
rmvList =["[',']','"','"',"]

work = pd.read_excel("STUDENTS_test.xlsx")




def main():
    ##newfile = work.drop(columns=['Progress','Last log in Dagile UK'])
    #work['Last Name'] = work['Last Name'].str.replace(" " ", "")
    #work['Last Name'] = work['Last Name'].str.replace('"', '')
    #work.replace('"', '')
    #work['Last Name'] = work['Last Name'].strip("'")

    #work.apply(lambda x:x.str.replace('"', ""))
    ##rep= work.loc[:,"Last Name"]
    ##rep.replace('"','', regex=True)
    #newfile.loc[work['Last Name'].isin(['Last Name'])] = ''
    ##name = input("Enter name of file: ")
    ##newfile.to_csv(f'{name}.csv') 
    ##print("task completed")
    pass


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
   
    print("task completed")



if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main_2()