abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# converting the text to thier index in the abc

def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
    return code

# converting code to txt

def code_to_txt(code):
    txt = []
    for number in code:
        txt.append(abc[number])
    return txt

# checking key length

def key_length(msg,key):
    while len(msg) > len(key):
        print("The key can not be shorter than the message.")
        key = input("Please give a key which length is equal to the message: ")
    return key

def encrypt(message,key):

    line_in_code = txt_to_code(message)
    key_in_code = txt_to_code(key_length(message,key))

    # encrypting with the key

    encrypted_message_code = []

    for i,v in enumerate(line_in_code):
        if v + key_in_code[i] < 26:
            encrypted_message_code.append(v + key_in_code[i])
        else:
            encrypted_message_code.append((v + key_in_code[i]) % 27)

    return ''.join(code_to_txt(encrypted_message_code))

def decrypt(enrcypted_message,key):

    enrcypted_message_code = txt_to_code(enrcypted_message)
    key_code = txt_to_code(key_length(enrcypted_message,key))

    # decrypting the message

    decrypted_message_code = []

    for i,v in enumerate(enrcypted_message_code):
        decrypted_message_code.append(v - key_code[i])

    return ''.join(code_to_txt(decrypted_message_code))
