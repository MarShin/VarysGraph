from twilio.rest import Client
from twitter import settings
class Alert:
    # Need ~9seconds for sms to arrive
    # Every sms cost $0.04 HKD
    @classmethod
    def send_sms(cls, to_number, text='Alert from GraphAlert'):
        if to_number is None:
            print 'missing phone number'
            print
            logging.debug('SMS Receiver phone number missing')
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            to=to_number,
            from_="+14156502580",
            body=text)
        print 'SMS sent: ' + str(message.sid)

    @classmethod
    def send_email(cls, to_email, text='Alert from GraphAlert'):
        pass
