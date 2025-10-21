def show_messages(messages):

# I start off by printing each message from a list of messages
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
   
# I send each message, moving it to sent_messages after sending
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Hey there!",
    "How are you?",
    "Let's play golf tomorrow!",
    "Good luck on your test!"
]

sent_messages = []

send_messages(text_messages, sent_messages)

print("\nFinal lists:")
print(f"Text messages: {text_messages}")
print(f"Sent messages: {sent_messages}")
