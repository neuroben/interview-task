#   - a rejtjelezett üzenet n. karaktere az üzenet n. karakterének kódja + kulcs n. karakterének kódja
# üzenet: "hello world"
# kulcs:  "abcdefgijkl" <---  hiányzik a H-betű ---> jó "abcdefghijk"
# rejtjelezett üzenet: "hfnosauzun"
# 7 4 11 11 14 26 22 14 17 11 3
# 0 1 2  3  4  5  6  7  8  9  10
# 7 5 13 14 18 4  1  21   25 20 13
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

line_in = input("Message: ")
key_in = input("Key: ")

line_in_code = []
key_in_code = []

encrypted_message_code = []
encrypted_message = []

# converting the text to thier index in the abc

def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
    return code

line_in_code = txt_to_code(line_in)
key_in_code = txt_to_code(key_in)

# reviewing the key length relative to the message

while len(line_in_code) > len(key_in_code):
    print("The key can not be shorter than the message.")
    key_in_code = txt_to_code(input("Please give a key which length is equal to the message: "))

# encrypting with the key

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










