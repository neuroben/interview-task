from crypto_functions import *

m1 = "uyvxiqzvwqsbvdrihuqpdorc"
m2 = "uyrelwk vzsxfrvwpj otbzb"
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
words = ["have", "a", "nice", "new", "day", "i", "wish", "you", "good", "luck"]
words_code = []
#print(abc.index("x"))

#converting txt to code

m1_code = txt_to_code(m1)
m2_code = txt_to_code(m2)

for word in words:
    words_code.append(txt_to_code(word))

#  print(words_code)

#  testing down || enrcypted_code - message = key
#  megpróbálni visszaafejteni mind a kettőt és a kulcsokat egymásra alkalmazni


word_code = txt_to_code("have")

def check(word:list):

    m1_ans = []
    for i,v in enumerate(m1_code[:len(word_code)]):
        v -= word_code[i]
        m1_ans.append(v)

    m2_ans = []
    for i,v in enumerate(m2_code[:len(word_code)]):
        v -= word_code[i]
        m2_ans.append(v)

    return m1_ans, m2_ans



print(''.join(code_to_txt(check(word_code)[0])))
print(''.join(code_to_txt(check(word_code)[1])))


