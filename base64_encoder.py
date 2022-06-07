import base64

message = input("text: ")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
print(base64_bytes.decode('ascii'))