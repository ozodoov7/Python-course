tuple=(11,12,13,14,15,16,17,18,19,20)
# print(tuple)
# print(tuple[1])
# print(tuple[2:8])
# print(tuple[:7])
# print(tuple[3:])
# print(tuple[2:9:2])
# print(tuple[::-1])
# print(tuple[-1])

# print("Exists") if 13 in tuple else print("not exits")

# for i in tuple: print(i, end=" ")

# n1
# narxlar = (2, 3, 4, 5, 1, 8, 7)
# even=0
# odd=0
# for i in narxlar:
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Juft narxalr yig'igndisi: {even}")
# print(f"Toq narxalr yig'igndisi: {odd}")

# n2
# kelganlar = (1, 2, 6, 4, 3, 7, 9, 10)
# for i in range(11):
#     if not i in kelganlar:
#         print(i, end=" ")

# n3
# jamoa1 = (1, 2, 3, 4)
# jamoa2 = (3, 5, 2, 1)
# jamoa3 = (2, 2, 3, 1)
# for i in range(4):
#     Sum=0
#     Sum=jamoa1[i]+jamoa2[i]+jamoa3[i]
#     print(f"{i+1} turda {Sum}")


# n4
# shaharlar = ("Toshkent", 
#              "Samarqand", 
#              "Toshkent", 
#              "Buxoro", 
#              "Samarqand", 
#              "Toshkent")
# amount=[]
# for i in shaharlar:
#     cnt=0
#     for j in shaharlar:
#         if i==j:
#             cnt+=1
#     amount[i]=cnt

# print(max(amount)) ## qayta ishlash kerak

#n8
# ombor = (45, 8, 23, 3, 67, 10, 5)
# for i in range(len(ombor)):
#     if ombor[i]<=10:
#         print(f"{i}-indeks {ombor[i]} dona qolgan")
    
# n9
# lst = [2, 12, 4, 3, 6, 15, 20, 30, 8, 1]
# for i in lst:
#     if i<5:
#         lst.remove(i)
# print(lst)

# n10
# lst = [2,3,32,22,43,25,87,45,9,34]
# print(max(lst))
# print(min(lst))

# n11
# n=10

# List=['apple', 5, True, 'apple',
#       'banana', 'google', 5,
#       'banana', False, 'banana']
# for i in range(10+1):
#     cnt=0
#     for j in range(10+1):
#         if list[i]==list[j]:
#             cnt+=1
#             print(List[i])
#     if cnt>=2:
#         print(List[i])

#try to change smth

import turtle

# Ekranni tayyorlash
t = turtle.Pen()
turtle.bgcolor('black') # Orqa fon qora bo'lsa, ranglar yorqin ko'rinadi
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# Foydalanuvchidan miqdorni so'rash
n = int(turtle.numinput("Savol", "Nechta chiziq chizaylik?", 100))
turtle.speed(1)
for x in range(n):
    # Rangni tanlash (qoldiq operatori % juda muhim!)
    t.pencolor(colors[x % 5]) 
    
    # Chiziq chizish va burilish
    t.forward(x*5) 
    t.left(74) # Mana shu burchakni o'zgartirib turli natijalar oling
    t.width(x * 6 / 100 + 1) # Chiziq qalinligi ham o'sib boradi

turtle.done()