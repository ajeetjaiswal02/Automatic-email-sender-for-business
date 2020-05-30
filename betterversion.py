# importing smptlib for connecting to emails
import smtplib # immporting smptlib
smtpt_object = smtplib.SMTP('smtp.gmail.com',587)
smtpt_object.ehlo() # use for greeting  the mail
smtpt_object.starttls() # for securtuty connection

import getpass
email = getpass.getpass("Enter your Email: ")
password = getpass.getpass("Enter Your Password:  ")
smtpt_object.login(email,password)


from_address = getpass.getpass("Enter Your Email: ")
to_address = getpass.getpass("Enter email of Recipents: ")
subject = input("Enter the Subject line: ")
message = input("Enter your message here:  ")
msg = "Subject: " + subject + '\n' + message
smtpt_object.sendmail(from_address,to_address,msg)

smtpt_object.quit()
