m1 = "uyvxiqzvwqsbvdrihuqpdorc"
m2 = "uyrelwk vzsxfrvwpj otbzb"
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
words = ["have", "a", "nice", "new", "day", "i", "wish", "you", "good", "luck"]
words_code = []

# converting letters to indexes in the abc

def txt_to_code(txt):
    code = []
    for letter in txt:
        code.append(abc.index(letter))
    return code


for word in words:
    words_code.append(txt_to_code(word))


m1_code = txt_to_code(m1)
m2_code = txt_to_code(m2)

# trying words into the encrypted messages

key = ""

for word in words_code:
    for number in range(len(word)):

