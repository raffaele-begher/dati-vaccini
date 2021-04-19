import os
from twilio.rest import Client

def send_msg(dati):
    client = Client('ACfe2d41c08a9d9340149128972ee41980', '5e2d30487a0874e504b20958616bed88')
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:+393663333940'
    message = client.messages.create(body = dati,
                          from_ = from_whatsapp_number,
                          to = to_whatsapp_number)
    print(message.sid)


