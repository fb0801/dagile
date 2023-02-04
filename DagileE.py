import smtplib, ssl, csv
import pandas as pd
import numpy as np
import os

import win32com.client
ol=win32com.client.Dispatch("outlook.application")
olmailitem=0x0 #size of the new email
newmail=ol.CreateItem(olmailitem)
newmail.Subject= 'Dagile Exit Questionnaire test'
#newmail.CC='xyz@gmail.com'


with open("test.csv") as work:
        #reader =pd.read_csv("test.csv")
        reader = csv.reader(work)
        next(reader)
        for esf, name, email in reader:
            newmail.sendmail(email,newmail.Body.format(FirstName=name, ID=esf),)

newmail.To=email




newmail.Body= """Subject: Email automation Test

    Subject: Email automation Test
    
    Dear {FirstName},
    your ID is {ID}
    automated python email test

    Farhan"""


print("Email sent")

# newmail.Attachments.Add(attach)
# To display the mail before sending it
# newmail.Display() 
newmail.Send()