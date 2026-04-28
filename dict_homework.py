# N1
# cars = {
#     "Malibu": 35000,
#     "Spark": 12000,
#     "Cobalt": 18000,
#     "Tracker": 28000
# }

# a=max(cars.values())
# b=min(cars.values())
# print(f"Eng arzon va eng qimmat mashinalarning o'rtacha narxi {(a+b)/2}")

# n2
# movies = {
#     "Titanic": 1997,
#     "Avatar": 2009,
#     "Inception": 2010,
#     "Interstellar": 2014
# }

# for i in movies:
#     if movies[i] >2000:
#         print(i)

# n3
# speed = {
#     "Tesla": 250,
#     "BMW": 240,
#     "Mercedes": 260,
#     "Audi": 230
# }
# sorted_speed=sorted(speed.items(), key=lambda x:x[1], reverse=True)
# print(sorted_speed)

# n4
# professions = {
#     "Bill Gates": "Dasturchi",
#     "Cristiano Ronaldo": "Futbolchi",
#     "Elon Musk": "Tadbirkor",
#     "Messi": "Futbolchi"
# }

# name=input("Ism kiriting: ")
# if name in professions:
#     print(professions[name])

# n5
# car_count = {
#     "Chevrolet": 120,
#     "Toyota": 95,
#     "BMW": 60,
#     "Kia": 75
# }

# a=max(car_count.values())
# b=min(car_count.values())

# for i in car_count:
#     if car_count[i] == a:
#         print(f"Eng ko'p sotilgan: {i}")
#     elif car_count[i] == b:
#         print(f"Eng kam sotilgan: {i}")

# n6
# books = {
#     "O'tkan kunlar": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1926,
#         "tarjimalar soni": 5
#     },
#     "Mehrobdan chayon": {
#         "muallifi": "Abdulla Qodiriy",
#         "janri": "Roman",
#         "chop etilgan yili": 1929,
#         "tarjimalar soni": 3
#     },
#     "Kecha va kunduz": {
#         "muallifi": "Cho'lpon",
#         "janri": "Roman",
#         "chop etilgan yili": 1934,
#         "tarjimalar soni": 4
#     },
#     "Sarob": {
#         "muallifi": "Abdulla Qahhor",
#         "janri": "Roman",
#         "chop etilgan yili": 1935,
#         "tarjimalar soni": 2
#     },
#     "Ulug'bek xazinasi": {
#         "muallifi": "Odil Yoqubov",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1974,
#         "tarjimalar soni": 6
#     },
#     "Don Kixot": {
#         "muallifi": "Migel de Servantes",
#         "janri": "Roman",
#         "chop etilgan yili": 1605,
#         "tarjimalar soni": 50
#     },
#     "Urush va tinchlik": {
#         "muallifi": "Lev Tolstoy",
#         "janri": "Tarixiy roman",
#         "chop etilgan yili": 1869,
#         "tarjimalar soni": 45
#     },
#     "Alkimyogar": {
#         "muallifi": "Paulo Koelyo",
#         "janri": "Falsafiy roman",
#         "chop etilgan yili": 1988,
#         "tarjimalar soni": 80
#     },
#     "1984": {
#         "muallifi": "Jorj Oruell",
#         "janri": "Antiutopik roman",
#         "chop etilgan yili": 1949,
#         "tarjimalar soni": 65
#     },
#     "Kichkina shahzoda": {
#         "muallifi": "Antuan de Sent-Ekzyuperi",
#         "janri": "Falsafiy ertak",
#         "chop etilgan yili": 1943,
#         "tarjimalar soni": 300
#     }
# }
# book=input("Kitob nomini kiriting: ")
# book=book.lower()
# for i in books:
#     if i.lower() == book:
#         print(books[i])
