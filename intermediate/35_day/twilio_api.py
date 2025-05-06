from twilio.rest import Client

# Your account sid and auth token from twilio.com/console
#DANGER! This is insecure . See twil.io/secure

#example

account_sid  = 'aksjdkq232k1jbas *exemplo*' 
auth_token = 'your auth token'

message = client.messages \
                .create(
                    body = "Join Eartj's mightiest heroes. Like... "
                    from_='#your number phone'
                    to='numero a ser enviado a mensagem'
                )

print(message.sid)