def encrypt(message,key):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    # converting the text to thier index in the abc

    def txt_to_code(txt):
        code = []
        for letter in txt:
            code.append(abc.index(letter))
        return code

    line_in_code = txt_to_code(message)
    key_in_code = txt_to_code(key)

    # reviewing the key length relative to the message

    while len(line_in_code) > len(key_in_code):
        print("The key can not be shorter than the message.")
        key_in_code = input("Please give a key which length is equal to the message: ")

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

    return ''.join(code_to_txt(encrypted_message_code))

def decrypt(enrcypted_message,key):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    
    # converting the text to thier index in the abc

    def txt_to_code(txt):
        code = []
        for letter in txt:
            code.append(abc.index(letter))
        return code

    enrcypted_message_code = txt_to_code(enrcypted_message)
    key_code = txt_to_code(key)

    # reviewing the key length relative to the encrypted message

    while len(enrcypted_message_code) > len(key_code):
        print("The key can not be shorter than the message.")
        key = input("Please give a key which length is equal to the message: ")

    # decrypting the message

    decrypted_message_code = []

    for i,v in enumerate(enrcypted_message_code):
        decrypted_message_code.append(v - key_code[i])

    # converting code to txt

    def code_to_txt(code):
        txt = []
        for number in code:
            txt.append(abc[number])
        return txt

    return ''.join(code_to_txt(decrypted_message_code))