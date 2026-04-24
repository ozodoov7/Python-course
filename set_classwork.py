# set1={1,2,3,4,5,8,54,32,54,98,65}
# print(set1)

# for i in set1:
    # print(i, end=" ")

# set2 = {"Olma","Anor", 'Gilos', "O'rik"}
# if "Anor" in set2:
#     print("Yes")
# else:
#     print("No")
# set1 = {'olma', 'anor', 'gilos', 'banan', 'uzum'}
# set2 = {'qovun', 'tarvuz', 'uzum', 'banan', 'olma'}

# set3 = set1.intersection(set2)
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2)
# set3 = set2.difference(set1)
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)


# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {4,5,6}

# print(set2.issubset(set1))
# print(set1.issuperset(set2))


# n1
# set1 = {"Artel", "Alif", "Yandex", "Google", "Meta"}
# set2 = {"Google", "Apple", "Amazon", "Meta"}
# set3 = {"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

# print(set1&set2&set3)

# n2
# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5, 6, 7, 8, 9}

# s1=set1.symmetric_difference(set2)
# print(sum(s1))

# n3
# set1 = {100, 20, 45, 80, 70, 50}
# set2 = {30, 55, 70, 60, 20, 100}

# set3=set1.intersection(set2)

# lst=[]

# for i in set3:
#     if i>60:
#         lst.append(i)

# print(lst)
# print(sum(lst)//len(lst))

# n4
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# set3=set1.union(set2)
# for i in set3:
#     if i % 2 == 0:
#         print(i)

# n5
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = {3, 4, 5}
# a=set1.intersection(set2)
# b=set1.intersection(set3)
# c=set2.intersection(set3)
# print(a.union(b,c))
# set4=set1&set2 | set1&set3 | set2&set3
# print(set4)

# n6
# set1 = {1, 3, 5, 6, 8}
# set2 = {3, 6, 9}
# set1.difference_update(set2)
# t=1
# for i in set1:
#     if i%2==1:
#         t*=i
# print(t)

# n7
# lst=["olma", "nok", "olma", "uzum", "nok"]
# set1=set()
# duplicates=[]

# for i in lst:
#     if i in set1:
#         duplicates.append(i)
#     else:
#         set1.add(i)
# lst=set(lst)
# print(duplicates)
# print(len(set1))

# n8
# set1 = {2, 3, 4, 5}
# set2 = {3, 4, 5, 6}
# set3=set1.intersection(set2)
# total=0
# for i in set3:
#     total+=i**2
# print(total)

# n9
# set1={4, 7, 1, 9, 3, 6}
# set1.remove(max(set1))
# set1.remove(min(set1))
# t=0
# print(sum(set1)/len(set1))

# n10
set1 = {1, 2, 3}
set2 = {2, 4, 5}
set3 = {3, 5, 6}


print((set1 - set2 - set3) | (set2 - set1 - set3) | (set3 - set1 - set2))