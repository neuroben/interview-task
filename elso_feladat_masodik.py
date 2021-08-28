abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

enrcypted_message_in = input("Encrypted message: ")
key_in = input("Enter key: ")

# reviewing the key length relative to the encrypted message

while len(enrcypted_message_in) > len(key_in):
    print("The key can not be shorter than the message.")
    key_in = input("Please give a key which length is equal to the message: ")

# converting inputs to code

def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
    return code

enrcypted_message_code = txt_to_code(enrcypted_message_in)
key_code = txt_to_code(key_in)
    
# decrypting the message

decrypted_message_code = []

for i,v in enumerate(enrcypted_message_code):
    if v - key_code[i] > 0:
        decrypted_message_code.append(v - key_code[i])
    else:
        decrypted_message_code.append((v - key_code[i]))
        
# converting code to txt

def code_to_txt(code):
    txt = []
    for number in code:
        txt.append(abc[number])
    return txt

decrypted_message = ''.join(code_to_txt(decrypted_message_code))

print('Encrypted message:',decrypted_message)