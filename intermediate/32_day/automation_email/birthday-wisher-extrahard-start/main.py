##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib

# 1. Ler o arquivo birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")

# 2. Verificar a data atual
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# 3. Criar um dicionário com aniversários
birthdays_dict = {(row.month, row.day): row for index, row in birthdays_df.iterrows()}

# 4. Verificar se hoje é aniversário de alguém
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    # 5. Escolher uma carta aleatória
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
        letter_contents = letter_file.read()
        personalized_letter = letter_contents.replace("[NAME]", name)

    # 6. Enviar o e-mail
    my_email = "your_email@example.com"
    password = "your_password"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )
