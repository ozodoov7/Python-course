# n1
# import datetime as d
# t=d.datetime.now()
# print(t)

# n2
# from datetime import date
# def count_days():
#     yil=int((input("Yil: ")))
#     oy=int((input("Oy: ")))
#     kun=int(input("Kun: "))

#     b_day=date(yil, oy, kun)
#     t=date.today()
#     diff=t-b_day
#     print(diff)

# count_days()

# n3
# from datetime import date
# def count_independence_day():
#     oy=9
#     kun=1
#     yil=2026
#     i_day=date(yil, oy, kun)
#     t=date.today()
#     print(i_day-t)

# count_independence_day()

# n4
# def add_matrix(a: list, b: list):
#     new_matrix=[]
#     for i in range(len(a)):
#         temp=[]
#         for j in range(len(a)):
#             temp.append(a[i][j]+b[i][j])
#         new_matrix.append(temp)
#     print(new_matrix)

# A = [
#     [1, 2],
#     [3, 4]
# ]

# B = [
#     [5, 6],
#     [7, 8]
# ]
# add_matrix(A, B)

# n5
# from translate import Translator
# def translate_to_en(a:list):
#     tarjimon=Translator(to_lang="en", from_lang="uz")
#     d={}
#     for i in a:
#         if type(i)==str:
#             text=tarjimon.translate(i)
#             d[i]=text
#     print(d)

# lst=["salom", "dastur", 2.5, "yordam", 34, "kitob"]
# translate_to_en(lst)

# n6
# def show_actor(d: dict):
#     try:
#         movie=input("Film nomini kiriting: ")
#         actor=d[movie]
#         print(actor)
#     except KeyError:
#         print("Bunday film yo'q")


# filmlar = {
#     "Titanic": "Jack Dawson",
#     "Harry Potter": "Harry Potter",
#     "The Dark Knight": "Bruce Wayne (Batman)",
#     "The Matrix": "Neo (Thomas Anderson)",
#     "Forrest Gump": "Forrest Gump",
#     "Gladiator": "Maximus Decimus Meridius",
#     "Inception": "Dom Cobb",
#     "Spider-Man": "Peter Parker",
#     "Iron Man": "Tony Stark",
#     "The Lord of the Rings": "Frodo Baggins"
# }

# show_actor(filmlar)