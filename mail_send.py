#Frist import smtlib : This is use for make connection with server
import smtplib

# Define a fnction which we can call later
def sender_mail():
# define the sende_email which you wan't to mail with
    sender_email = "xyz@mail.com"
# ENter the pass word of your mail you can also assign his in other file and hen import it on main file       
    password = input(str("Please enter your password: "))
# Enter the recieve mail for which you want to make the mail recieve    
    rec_email = input(str("enter the emails where email have to be sent: "))
# define subject desigm or structure    
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server  = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login(sender_email, password)
    print("login success")
    server.sendmail(sender_email, rec_email, message)
    print("Email has benn sent to ", rec_email)

subject = 'Thank you for using Automatic mail' 
msg = 'Dear user Our Team will contact you in next 24 hours For further deatils\nThank you\nAutomatic mail'   
sender_mail()


# thank you for usinfg this repository  more more content ping me in this