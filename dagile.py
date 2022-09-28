'''Python script to read two files and see if they are there otherwise add them'''

def read_file_one():
   with open("STUDENTS_spreadsheet.xlsx", 'r') as f:
        for line in f:
            if "" in line:
            # found = True # Not necessary
                return True
        return False 



def read_file_two():
    with open("", 'r') as g:
        pass


def write_file():
    with open("", 'w+') as h:
        pass 


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    read_file_one()