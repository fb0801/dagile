'''application to fix the file 
part of https://github.com/fb0801/dagile created by Farhan


'''

#application modules
import pandas as pd
import numpy as np

rmv =['A','B','T','U']

#work = pd.read_excel("STUDENTS_test.xlsx")



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

'''
Remove the square brackets and quotation marks from the ‘groups’ column by highlighting the column, pressing ctrl + F, 
search for [ , leave the ‘replace with’ field blank then select ‘replace all’. Repeat for ] and “:
'''

def main_2():
    #data_top = work.head()  
    #print(data_top) 
    #newfile = work.drop(columns=['A','B','T','U'] axis=1)
    newfile = work.drop(columns=['User Status', 'Tutor','password','groups'])
    #newfile = work.drop(['A','B','T','U'], axis=1)
    ##newfile = work.pop(rmv)  
     #rep= work.loc[:,"groups"]
     #rep.replace('"','', regex=True)

    ##name = input("Enter name of file: ")
    ##newfile.to_csv(f'{name}.csv') 
    ##print("task completed")



if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main_2()