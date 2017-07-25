from twilio.rest import Client

class Alert:


# Your Account SID & Token from twilio.com/console
# testing ac
# ACa5466a67cec062d381ed666904c6c5da
# 7c40960d8d9643d435981cedb09dc9c3

# Actual
# AC7dc30be782c0963fc33412a088cfb308
# b1fbdc32de31521d7132f84893e5ace3

    def send_sms(to_number, text='Alert from AlertGraph'):
        account_sid = "AC7dc30be782c0963fc33412a088cfb308"
        auth_token  = "b1fbdc32de31521d7132f84893e5ace3"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=to_number,
            from_="+14156502580",
            body=text)

        print 'SMS sent: ' + str(message.sid)
