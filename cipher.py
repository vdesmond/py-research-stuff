import string

alphabet = " " + string.ascii_lowercase
positions = {alphabet[i]: i for i in range(len(alphabet))}


def encoding(message, key):
    result = [(positions[i] + key) % 27 for i in message]
    encoded_message = "".join([alphabet[i] for i in result])
    return encoded_message


decoded_message = encoding(message="hi my name is caesar", key=3)
reencoded_message = encoding(decoded_message, key=-3)
print(reencoded_message)