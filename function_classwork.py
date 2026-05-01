# def salom_ber():
#     print("Salom hammaga")

# salom_ber()
# salom_ber()
# salom_ber()

# def func1():
#     pass

# def func2(a, b):
#     print(a + b)
# func2("Salom ", "Dunyo")
# func2("Salom ", 11)

# def func3(a, b):
#     c = a+b65
#     return c

# print(func3(2,5))

# def func4(a, b):
#     c = a + b
#     d = a * b
#     return c, d
# a, b = func4(4,6)
# print(a, b)
# print(func4(4,6))

# def func5(a,b,c=0):
#     print(a+b+c)
# func5(3,4)

# def func6(a:int, b:int) -> int:
#     print(a+b)
#     return a*b
# a=func6(4, 5)
# print(a)

# def func7(*a):
#     print(a)

# func7(2,3,4,5,6,7,8,9)

# def func8(**n):
#     print(n)
#     print(n['ism'])
# func8(yosh=15, ism='Alisher', guruh="N205")

# def func9(a, b):
#     return a+b

# func10=lambda a,b : a+b
# print(func10(4,5))
# print(func9(4,5))

# def musbat(a:list, b:list):
#     for i in a:
#         if i>0:
#             b.append(i)
#     return b

# a=[1, -1, 2, 9, -3, -11, 20, 5, -8, 4]
# b=[]
# print(musbat(a,b))

# def katta_harf(dict1):
#     result={}
#     for keys, values in dict1.items():
#         upper_l=values.upper()
#         result[keys]=upper_l
#     return result
# dict1= {
# 	"Ism": "Ali",
# 	"Familya": "Kamolov",
# 	"Manzil": "Angren shahri"
# }
# b=katta_harf(dict1)
# print(b)


# def extend_lists(list1, list2):
#     result={}
#     for i in range(len(list1)):
#         result[list1[i]]=list2[i]
#     return result

# list1=["Jon", "Jeyms", "Piter", "Tony"]
# list2=["Vik", "Bond", "Parker", "Stark"]

# a=extend_lists(list1, list2)
# print(a)


# lst1=[10,23,32,45,87,80,17]

# lst2=[]
# for i in lst1:
#     if i%2==0:
#         lst2.append(i)
# print(lst2)

# def is_even(n):
#     return n%2==0
# lst2=list(filter(is_even, lst1))
# print(lst2)

# lst2=list(filter(lambda n: n%2==0, lst1))
# print(lst2)

# def summ (nums):
#     if len (nums) == 0:
#         return 0
#     a = nums[0]
#     b = nums[1:]
#     return (a if a % 2 == 0 else 0) + summ (b)
# t = (2,3,5,6,3,7,8,4)
# print(summ(t))

# def func(*n):
#     return sum(n)//len(n)
# print(func(2,3,4,7,8,6,5))

# def func(**data):
#     if 'umumiy' in data:
#         umumiy=data['umumiy']
#         chegirma=data.get('chegirma', 0)
#         return umumiy - chegirma
#     return "Umumiy qiymat berilmagan"
# print(func(umumiy=550, chegirma=70))

# func=lambda a,b: b if a<b else a
# print(func(4,5))

func=lambda n: sum(n)/len(n) if n else 0
my_tuple = (2, 3, 4, 7, 8, 6, 5)

print(func(my_tuple))