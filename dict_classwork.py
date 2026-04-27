# car = {
#     "brand" : "Tayota",
#     "model" : "Camry",
#     "rang" : "black",
#     "narx" : 45_000,
#     "type" : "sedan",
#     "rang" : "blue" # oxirgi qo'shilgan qoladi oldingisi o'chib ketadi
# }
# print(car)
# car["model"]="Land Cruiser"
# print(car)
# car["yil"] = 2025
# print(car)
# if "type" in car:
    # print(True)
# else:
    # print(False)

# for i in car:
    # print(i, car[i])

# print(car["yil"])
# print(car.get('yil', "topilmadi"))

# print(list(car.keys()))

# print(list(car.values()))

# k = car.pop("probeg")
# print(car)
# print(k)

# car2 = car.copy()
# print(car2)

# print(car.items())
# for i,j in car.items():
#     print(i, j)

# car.clear()
# print(car)

# k = car.popitem()
# print(k)
# print(car)

# car['narx'] = 9000
# car['ish-turi'] = 'dastavka'
# car['probeg'] = 100000

# car.update({"narx": 9000, 'ish-turi':'dastavka', 'probeg':100000})
# print(car)

# n1
# students = {
# 	"Samandar": 18,
# 	"Muzaffar": 19,
# 	"Xojiakbar": 16,
# 	"Islom": 20,
# 	"Asomiddin": 14,
# 	"Sobitjon": 17,
# 	"Shoxruh": 20
# }

# for i in students:
#     if students[i]>18:
#         print(i)

# n2
# users = {
# 	"jeymsBond" : "agent007",
# 	"tony_stark": "ironman101",
#  	"piterParker": "spider.12.12",
# 	"sherlok": "sher.l04"
# 	}

# login=input("Loginni kiriting: ")
# if login in users:
#     parol=input("Parolni kiriting: ")
#     if parol == users[login]:
#         print("Hisobga kirdingiz!")
#     else:
#         print("Parolda xatolik")
# else:
#     print("Bunday login topilmadi")

# n3
# que=['S001', 'S002', 'S003', 'S004']
# names=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# nums=[85, 98, 89, 92]
# nested_dict={}
# for i in range(len(que)):
#     nested_dict.update({que[i] : {names[i]: nums[i]}})
# print(nested_dict)

# n4
lst=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
new_dict={}
for colour, num in lst:
    if colour in new_dict:
        new_dict[colour].append(num)
    else:
        new_dict[colour]=[num]
print(new_dict)