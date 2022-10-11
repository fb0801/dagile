'''application to fix the file'''

#application modules
import pandas as pd
import numpy as np



work = pd.read_excel("STUDENTS_spreadsheet.xlsx") 


def main():
    newfile = work.drop(columns=['Progress','Last log in Dagile UK'])

    newfile.to_csv('file_name.csv') 
    print("task completed")

if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()