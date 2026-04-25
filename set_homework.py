# n1
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# print(sum(set1.difference(set2)))

# n2
# set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
# set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
# set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

# set1.intersection_update(set2)
# set1.difference_update(set3)
# print(set1)

# n3
# set1 = {1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
# set1.intersection_update(set2)
# lst=[]
# for i in set1:
#     lst.append(i)
# lst.sort(reverse=True)
# print(lst)

# n4
# ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
# vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}
# print(ali.intersection(vali))
# print(ali.difference(vali))

# n5
# set1=input(">>>> ")
# set2=input(">>>> ")
# set1=set(set1)
# set2=set(set2)
# if set1.issuperset(set2):
#     print(True)
# else:
#     print(False)

# n6
# set1={4,5,6,7,8,9}
# set2={5,6,7,10,11}

# u=set()
# u=set1.intersection(set2)
# d=set()
# d=set1.difference(set2).union(set2.difference(set1))
# print(sum(d)-sum(u))