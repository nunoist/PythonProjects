from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC95ae6d5717bcdff03d28304f0fe7235b"
auth_token  = "4048e3ec2f61af01df7f05f8ea2f2e46"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+447789333630",    # Replace with your phone number
    from_="+441315103498") # Replace with your Twilio number
print message.sid
