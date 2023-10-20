from twilio.rest import Client

account_sid = 'AC3e38fc8efcfd2736707615630aa5509a'
auth_token = '21b05d1b27c6993e81a1b1acbff95adf'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body='bring an umbrella☂️',
    from_='+18787688918',
    to='+213797873139'
)
print(message.status)
