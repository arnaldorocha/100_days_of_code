import smtplib

my_email = "endereço do email" #email@gmail.com
password = "senha" #sua senha

# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="endereço email para enviar mensagem", 
#     msg= "Subject: Hello\n\nThis is the body of my email")
# connection.close()


with smtplib.SMTP("smtp.gmail.com") as connection: # usando with pra nao usar  connection.close()
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="endereço email para enviar mensagem", 
        msg= "Subject: Hello\n\nThis is the body of my email"
        )
    