# f=open("text.txt", 'w')
# print(f.read())

# line=f.readlines()
# print(line)

# for i in f:
#     print(i, end="")

# f.writable()
# print(f.writable())

# sonlar=[2, 3, 4, 7, 8, 6, 5]

# for i in sonlar:
#     f.write(f"{i} ")
# f.close()

# file=open("text.txt")
# sonlar=file.read()
# sonlar=list(map(int, sonlar.split()))
# print(sonlar)
# print(sum(sonlar))

# import random
# def get_random():
#     nums=[]
#     for i in range(10):
#         a=random.randint(1,10)
#         nums.append(a)
#     return nums
# nums=get_random()

# file=open("text.txt", 'w')
# for i in nums:
#     file.write(f"{i} ")

# import math

# file1=open("text.txt")
# file2=open("Ildiz.txt", 'w')

# sonlar=file1.read()
# sonlar=list(map(int, sonlar.split()))
# for i in sonlar:
#     file2.write(f"{math.sqrt(i)} ")

# countries=open("countries.txt")
# capitals=open("capitals.txt")
# d=countries.read()
# d=list(map(str, d.split()))
# c=capitals.read()
# c=list(map(str, c.split()))

# new=open("New.txt", 'w')
# for i in range(len(d)):
#     new.write(f"{d[i]} - {c[i]}\n")

# from translate import Translator as t

# file=open("t.txt")
# text=file.read()
# text=list(map(str, text.split()))
# t=open("tarjima.txt", 'w')

# for i in text:
#     t.write(f"{t.translate('en', i)}")

# JSON
# import os
# os.system("cls")
import json

# users= [
#     {
#         "username": "ozodoov__",
#         "followers":500,
#         "following": 100,
#         "posts_count": 0
#     },
#     {
#         "username": "suhrob",
#         "followers":500,
#         "following": 1200,
#         "posts_count": 6000
#     },
#     {
#         "username": "Sherali",
#         "followers":220,
#         "following": 340,
#         "posts_count": 32
#     },
#     {
#         "username": "Ayubxon",
#         "followers":5000,
#         "following": 280,
#         "posts_count": 40
#     }
# ]

# file = open("users.json", "w")
# json.dump(users, file, indent=2)

# file = open("users.json")
# users = json.load(file)
# print(users)

# n1
# ism=input("Ismingizni kiriting: ")
# familiya=input("Familiyangizni kiriting: ")
# yosh=int(input("Yoshingizni kiriting: "))
# manzil=input("Manzilni kiriting: ")
# telefon=input("Telofon raqamni kiriting: ")

# odam={}
# odam['Ism']=ism
# odam['Familiya']=familiya
# odam['Yosh']=yosh
# odam['Manzil']=manzil
# odam['Telefon']=telefon
# print(odam)

# file=open("Odam.json", 'w')
# json.dump(odam, file, indent=4)

# n2
# file=open("contacts.json", 'w')
# telefon_kitobi = {
#     "Alisher": "+998-90-123-45-67",
#     "Bobur": "+998-93-234-56-78",
#     "Charos": "+998-94-345-67-89",
#     "Doston": "+998-97-456-78-90",
#     "E'zoza": "+998-99-567-89-01",
#     "Farhod": "+998-88-678-90-12",
#     "Gulnoza": "+998-91-789-01-23",
#     "Hamid": "+998-95-890-12-34",
#     "Iroda": "+998-33-901-23-45",
#     "Jasur": "+998-77-012-34-56"
# }
# json.dump(telefon_kitobi, file, indent=4)

def find_user(a: dict):
    try:
        b=input("Ismni kiriting: ")
        print(f"{b} : {a[b]}")
    except:
        print("Bunday foydalanuvchi yo'q")

def add_user(a: dict):
    b=input("Ismni kiriting: ")
    num=input("Raqamni kiriting: ")
    a[b]=num


file=open("contacts.json")
users=json.load(file)
file.close()

find_user(users)
a=input("Foydalanuvchi qo'shasizmi?\n Y/N? ")
while a:
    add_user(users)
    print("Yana foydalanuvchi qo'shasizmi? ")
    a=input("Y/N? ")
    if a.lower()=='y':
        a=True
    elif a.lower()=='n':
        break

file=open("contacts.json", 'w')
json.dump(users, file, indent=4)

