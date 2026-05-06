import os
os.system("cls")

# try:
#     a=int(input(">>> "))
#     b=int(input(">>> "))
#     print(a/b)
# except ValueError:
#     print("Xatolik sodir bo'ldi")
# except ZeroDivisionError:
#     print("Sonni 0 ga bo'lib bo'lmaydi")
# else:
#     print(True)
# finally:
#     print("Dastur tugadi")

import math

# print(math.pow(5,4))
# print(math.sqrt(256))
# print(math.log2(16))
# print(math.log(64,2))
# print(math.floor(4.95))
# print(math.ceil(2.31))
# print(round(2.95), round(4.50001))

import random as r

# n=r.randint(1,100)
# print(n)

# m=r.uniform(1,10)
# print(round(m, 2))

# names=["Javohir", "Jahongir", "Muhammad", "Ilhom"]

# print(r.choice(names))
# print(r.choices(names, k=2))
# print(r.sample(names, k=2))

# r.shuffle(names)
# print(names)


# os.mkdir("Salom")
# os.rmdir("Salom")

# os.remove("temp")
# os.rename("temp", "Temp")

# import library as l
# print(l.find_even(5))

# import wikipedia as wk
# wk.set_lang("uz")
# page=wk.page("Cristiano Ronaldo")

# print(page.content)

# from translate import Translator
# tarjimon=Translator(to_lang="en", from_lang="uz")
# text=tarjimon.translate("qalaysan")
# print(text)

import cv2
camera=cv2.VideoCapture(0)
while True:
    is_valid, image=camera.read()
    if is_valid:
        cv2.imshow("Selfi", image)
    
    if cv2.waitKey(1) & 0xfff == 32: 
        break