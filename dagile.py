'''Python script to read two files and see if they are there otherwise add them'''

def read_file_one():
   with open("", 'r') as f:
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