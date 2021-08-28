abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

line_in = input("Message: ")
key_in = input("Key: ")

# reviewing the key length relative to the message

while len(line_in) > len(key_in):
    print("The key can not be shorter than the message.")
    key_in = input("Please give a key which length is equal to the message: ")

# converting the text to thier index in the abc

def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
    return code

line_in_code = txt_to_code(line_in)
key_in_code = txt_to_code(key_in)

# encrypting with the key

encrypted_message_code = []

for i,v in enumerate(line_in_code):
    if v + key_in_code[i] < 26:
        encrypted_message_code.append(v + key_in_code[i])
    else:
        encrypted_message_code.append((v + key_in_code[i]) % 27)

# convert the numbers to letters

def code_to_txt(code):
    txt = []
    for number in code:
        txt.append(abc[number])
    return txt

encrypted_message = ''.join(code_to_txt(encrypted_message_code))

print('Encrypted message:',encrypted_message)