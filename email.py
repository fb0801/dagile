from datetime import datetime
import pandas as pd

  
today = datetime.now()
    
month1 = today.strftime("%b")
print("Current Month Full Name:", month1);


work = pd.read_excel("", usecols=['ID', 'First Name', 'Last Name', 'Email Address', 'START DATE', 'Org.', 'Gender', 'End DATE','Completer/Early Leaver', 'Folllow up Progression in work '])


print(work)



#function to send emails
def SendEmail():
    pass
