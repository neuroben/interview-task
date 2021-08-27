#   - a rejtjelezett üzenet n. karaktere az üzenet n. karakterének kódja + kulcs n. karakterének kódja
# üzenet: "hello world"
# kulcs:  "abcdefgijkl" <---  hiányzik a H-betű ---> jó "abcdefghijkl"
# rejtjelezett üzenet: "hfnosauzun"
# 7 4 11 11 14 26 22 14 17 11 3
# 0 1 2  3  4  5  6  7  8  9  10
# 7 5 13 14 18 4  1  6  25 21 13
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

line_in = input("Message: ")
key_in = input("Key: ")

line_in_code = []
key_in_code = []

encrypted_message_code = []
encrypted_message = []



def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
        print(letter,abc.index(letter))
    return code

line_in_code = txt_to_code(line_in)
key_in_code = txt_to_code(key_in)

print(line_in_code,len(line_in_code))
print(key_in_code,len(key_in_code))






