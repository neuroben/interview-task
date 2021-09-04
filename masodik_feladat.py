from crypto_functions import *

raw_words = open("words.txt")
words = []
words_code = []
for line in raw_words:
    words.append(line.strip())
    words_code.append(txt_to_code(line.strip()))

m1 = "uyvxiqzvwqsbvdrihuqpdorc"
m2 = "uyrelwk vzsxfrvwpj otbzb"

m1_code = txt_to_code(m1)
m2_code = txt_to_code(m2)


# egyezes = 0
# egyezesek = []
# for i,v in enumerate(words):
#     if len(v) <= len(decrypt("rywnf","kulcs")):
#         for j,letter in enumerate(v):
#             if letter == decrypt("rywnf", "kulcs")[j]:
#                 print(v, decrypt("rywnf", "kulcs"))
#                 egyezes += 1
#                 print(letter)
#                 print(decrypt("rywnf", "kulcs")[j])
#                 egyezesek.append(v)
#             else:
#                 egyezes = 0
#         egyezes = 0
#
# print(egyezesek)
#
# print(decrypt("rywnf", "kulcs"))
# ans = []
#
# for word in words_code:
#     for i,v in enumerate(word):
#         ans.append(decrypt(m2[:len(word)],code_to_txt(m1_code[i] - v)))
#
#
#
# for j,w in enumerate(words_code):
#     print(w)
#     if len(w) > 1:
#         for i,letter in enumerate(w):
#             print(decrypt(code_to_txt(m1_code[i]),m1_code-letter))
#     else:
#         print(i)
#         print(decrypt(code_to_txt(m1_code[i]),m1_code-w))
# words_length = []
# words_length.append(0)
# for word in words:
#     words_length.append(len(word))
#
# start = 0
# end = 4
# ans = []
# for j, word in enumerate(words_code):
#     for i in range(words_length[i],words_length[i+1]):
#         ans.append(m1_code[i] - word[i])
#
# print(ans)
#
# for i,v in enumerate(words_code):
#     for j,w in enumerate(m1_code[:len(v)]):
#         key = alphabet(w - v[j])
#         key_code = w - v[j]
#         #print(key,end="")
#         print(v)
#         print(m2[:len(v)])
#         print(key)
#         print(decrypt(m2[:len(v)],key))
#     print()
#
#
#
#
# print(words)
# print(words_length)
# print(word)
#
# print(words_code)
#
#
#
#
# for w_index,word in enumerate(words_code):
#
#     def check(words):
#
#         m1_ans = []
#         for i,v in enumerate(m1_code[:len(words)]):
#             v -= words[i]
#             m1_ans.append(v)
#
#
#         m2_ans = []
#         for i,v in enumerate(m2_code[:len(words)]):
#             v -= words[i]
#             m2_ans.append(v)
#
#         return m1_ans, m2_ans
#
#     #m1
#     print(check(word)[1])
#     print(decrypt(m1[len(word)],''.join(code_to_txt(check(word)))))
#     #m2
#     print(check(word)[0])
#     print(decrypt(m2[len(word)],''.join(code_to_txt(check(word)[0]))))
#
#
#
#
#
#
# #m1
# print(decrypt("uyvxi","nyatj"))
# #m2
# print(decrypt("","nyatj"))
#
# print()
# print()
#
# #m1
# print(decrypt("iqzv","jcyr"))
# #m2
# print(decrypt("lwk","jcyr"))
#
# print()
# print()
#
# #m1
# print(check(word_code)[0])
# print(''.join(code_to_txt(check(word_code)[0])))
# #m2
# print(check(word_code)[1])
# print(''.join(code_to_txt(check(word_code)[1])))
#
# #def replacement(ans1,ans2):
