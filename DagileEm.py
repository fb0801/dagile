import smtplib, ssl, csv
import pandas as pd
import numpy as np
import os

def main():
    #sender, pwd = read_creds()
    #recieve = sender
    #esubject="Email automation Test"

    """email_string = f'''Subject: A plain text email
    To: {','.join(email_to)}
    This is a new test email sent by Python.'''"""

    message= """Subject: Email automation Test

    Subject: Email automation Test
    
    Dear {FirstName},
    your ID is {ID}
    automated python email test

    Farhan
    """

    
    #
    from_address = ""
    
    password=""

    context = ssl.create_default_context()
    print("Starting to send")
    #with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    
    with smtplib.SMTP_SSL("smtp.office365.com", 587, context=context) as server:
        server.login(from_address, password)
        #smtpObj = smtplib.SMTP_SSL('smtp-mail.outlook.com', 465)
        #server.starttls()
        #work =pd.read_csv("test.csv")
        with open("test.csv") as work:
            #reader =pd.read_csv("test.csv")
            reader = csv.reader(work)
            next(reader)
            for esf, name, email in reader:
                server.sendmail(from_address, email, message.format(FirstName=name, ID=esf),)
    print("Email sent")


if __name__ == "__main__":
    #takes user to the main menu using magic method/dunders
    main()