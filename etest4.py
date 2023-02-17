import win32com.client


ol=win32com.client.Dispatch("outlook.application") #uses outlook app


olmailitem=0x0 #size of the new email
newmail=ol.CreateItem(olmailitem)
newmail.Subject= 'Testing Mail'
newmail.To=''
#newmail.CC='xyz@gmail.com'
newmail.Body= "Subject: Email automation Test \nDear {FirstName},\n your ID is {ID} automated python email test \n from Farhan"
# attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
# newmail.Attachments.Add(attach)

# To display the mail before sending it
# newmail.Display() 


newmail.Send()
