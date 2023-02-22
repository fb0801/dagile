import win32com.client
import smtplib, ssl, csv
import pandas as pd
import numpy as np
import os


ol=win32com.client.Dispatch("outlook.application") #uses outlook app


olmailitem=0x0 #size of the new email
newmail=ol.CreateItem(olmailitem)
newmail.Subject= 'Testing Mail'

#newmail.CC='xyz@gmail.com'
#newmail.Body= "Subject: Email automation Test \nDear {FirstName},\n your ID is {ID} automated python email test \n from Farhan"
# attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
# newmail.Attachments.Add(attach)

# To display the mail before sending it
# newmail.Display() 


email_list = pd.read_csv("test.csv")
all_names = email_list['name']
all_emails = email_list['email']
all_esf = email_list['esf']


#loop through emails
for idx in range(len(email_list)):

    # Get each records name, email, subject and id
    name = all_names[idx]
    email = all_emails[idx]
    esf = all_esf[idx]

    # Create the email to send
    newmail.To= email #addr to send email
    
    newmail.Body= ("Subject: Email automation Test \n Dear {0},\n your ID is {1} automated python email test \n from Farhan").format(name,esf)



#newmail.Body= ("Subject: Email automation Test \nDear {FirstName},\n your ID is {ID} automated python email test \n from Farhan").format(FirstName=name, ID=esf)
print("Email sent")

newmail.Send()
