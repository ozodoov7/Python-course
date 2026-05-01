# n1
# def sort_null (lst: list):
#     nums=[]
#     nulls=[]
#     for i in lst:
#         if i == 0:
#             nulls.append(i)
#         else: 
#             nums.append(i)
#     nums=nums+nulls
#     return nums

# lst1=[3,4,0,0,0,6,2,0,6,7,6,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
# new_lst=sort_null(lst1)
# print(new_lst)

# n2
# def sort_dublicates (lst: list):
#     new_list=[]
#     for i in lst:
#         if i not in new_list:
#             new_list.append(i)
#     return(new_list)
        

# lst1=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_list=sort_dublicates(lst1)
# print(new_list)

# n3
# def add_lists(lst1, lst2):
#     lst3=[]
#     n=len(lst1)+len(lst2)
#     for i in range(n):
#         if i < len(lst1):
#             lst3.append(lst1[i])
#         if i < len(lst2):
#             lst3.append(lst2[i])
#     return(lst3)

# list1=[1, 2] 
# list2=[11, 22, 33, 44, 55]
# print(add_lists(list1, list2))

# n4
# def sort_same_nums(lst1, lst2):
#     new_list=[]
#     max_len=max(len(lst1), len(lst2))
#     for i in range(max_len):
#         if i<len(lst1) and lst1[i] in lst2:
#             new_list.append(lst1[i])
#         elif i<len(lst2) and lst2[i] in lst1:
#             new_list.append(lst2[i])
#         new_list=set(new_list)
#         new_list=list(new_list)
#         new_list.sort()
#     return(new_list)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(sort_same_nums(a, b))

# n5
# def dublicates(n: int):
#     lst=[]
#     for i in range(n):
#         lst.append(int(input("Son kiriting: ")))
#     dublicates=[]
#     for j in lst:
#         if lst.count(j)>1:
#             dublicates.append(j)
#     return (dublicates)

# N=int(input("Nechtalik list bo'lsin: "))
# print(dublicates(N))

# n6
# def sqrts(lst):
#     sqrts=[]
#     for i in lst:
#         a=(lambda i: i**2)(i)
#         sqrts.append(a)
#     return(sqrts)
# lst=[1,2,3,4,5,6,7,8,9,10]
# print(sqrts(lst))

# n7
# def to_dict(text):
#     char_dict={}
#     for char in text:
#         char_dict[char] = char_dict.get(char, 0) + 1
#     return(char_dict)
# text = 'w3resource'
# print(to_dict(text))
