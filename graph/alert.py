import os

from twilio.rest import Client
from twitter import settings
import sendgrid
from sendgrid.helpers.mail import *

class Alert:
    # Need ~9seconds for sms to arrive
    # Every sms cost $0.04 HKD
    @classmethod
    def send_sms(cls, to_number, text='Alert from Varys'):
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
    def send_email(cls, to_email='martinshin95@gmail.com', text='Alert from Varys'):
        sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
        from_email = Email("test@example.com")
        to_email = Email(to_email)
        subject = text
        content = Content("text/plain", "Please check the Varys Graph for more details")
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
