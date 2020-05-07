import smtplib

def sender_mail():

    sender_email = "desigmcorp@gmail.com"
    password = input(str("Please enter your password: "))
    rec_email = input(str("enter the emails where email have to be sent: "))
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server  = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login(sender_email, password)
    print("login success")
    server.sendmail(sender_email, rec_email, message)
    print("Email has benn sent to ", rec_email)

subject = 'Thank you for using Desigm' 
msg = 'Dear user Our Team will contact you in next 24 hours For further deatils\nThank you\nDesigm'   
sender_mail()