from twilio.rest import Client


ACCOUND_SID = 'AC133feac03c016fd584353b4aa05bfc4d' 
AUTH_TOKEN = '8e1c968c34efe74516c2d08718705640'
TWILIO_NUMBER = '+19855455408'

targetNumber = '+639292558823'
body = 'NAGANA NA BA OIDE'


client = Client(ACCOUND_SID,AUTH_TOKEN)

def sendSMS(targetNum, body):
    message = client.messages.create(
        body=body,
        from_ = TWILIO_NUMBER,
        to=targetNumber
    )
    print(message.body)

sendSMS(targetNumber,body)

