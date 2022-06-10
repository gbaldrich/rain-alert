# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC1320103e75aba45bfb585162f162c327'
auth_token = '96ed30f50f57a932476bc12577ddb69c'
client = Client(account_sid, auth_token)

def send_sms(to_number, message):
    """Send an SMS message."""
    message = client.messages \
        .create(
            to=to_number,
            from_='+12058466918',
            body=message)

    print(message.sid)