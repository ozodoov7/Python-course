# n1
# def find_words(a):
#     new_dict={}
#     for i in a:
#         new_dict[i]=new_dict.get(i, 0)+1
#     sorted_dict=sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
#     result=[]
#     for i in range(min(3, len(sorted_dict))):
#         result.append(sorted_dict[i][0])
#     return result


# gap="olma nok olma gilos olma nok shaftoli"
# gap=gap.split()
# d=find_words(gap)
# print(d)

# n2
# def find_avg(a: dict):
#     for i, k in a.items():
#         score1=[]
#         for j in k.values():
#             score1.append(j)
#         print(f"{i}: {sum(score1)/len(score1)}")
    
# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
# }
# find_avg(students)

# n3
# def find_min(l: list):
#     total=0
#     for i in l:
#         total+=i['miqdor']
#     sorted_dict=sorted(l, key=lambda x:x['miqdor'])   

#     print(f"Umumiy mahsulotlar miqdori: {total}")
#     print('Eng kam qolgan 3 ta mahsulot:', end=" ")
   
#     for i in range(3):
#         print(sorted_dict[i]['mahsulot'], end=", ")

# ombor = [
#     {"mahsulot": "olma", "miqdor": 5},
#     {"mahsulot": "nok", "miqdor": 9},
#     {"mahsulot": "shaftoli", "miqdor": 7},
#     {"mahsulot": "anor", "miqdor": 4},
#     {"mahsulot": "banan", "miqdor": 6},
#     {"mahsulot": "uzum", "miqdor": 8},
#     {"mahsulot": "gilos", "miqdor": 2},
#     {"mahsulot": "tarvuz", "miqdor": 1},
#     {"mahsulot": "qovun", "miqdor": 3},
#     {"mahsulot": "limon", "miqdor": 5}
# ]
# find_min(ombor)

# n4
# def sort_value(d: dict):
#     sorted_dict=sorted(d, key=lambda x:d[x])
#     for i in sorted_dict:
#         print(i)
#     # print(sorted_dict)
# my_dict = {
#     "t": 3,
#     "p": 1,
#     "y": 2,
#     "o": 5,
#     "h": 4,
#     "n": 6,
# }
# sort_value(my_dict)

# n5
# def del_dubs(l:list):
#     l=set(l)
#     l=list(l)
#     for i in l:
#         if i == "":
#             l.remove(i)
#     print(l)
# mylist = ["olma", "", "olma", "gilos", ""]
# del_dubs(mylist)