from twilio.rest import Client
from twitter import settings

class Alert:

    def send_sms(to_number, text='Alert from AlertGraph'):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=to_number,
            from_="+14156502580",
            body=text)
        print 'SMS sent: ' + str(message.sid)

    def send_email(to_email, text='Alert from AlertGraph'):
        pass
