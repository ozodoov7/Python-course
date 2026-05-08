# type easy
# n1
# def square_nums(a):
#     squares=[]
#     for i in a:
#         squares.append(i**2)
#     return squares

# n=[1,2,3,4,5,6,7,8,9]
# print(square_nums(n))

# n2
# def extract_even_nums(a):
#     evens=[]
#     for i in a:
#         if i%2==0:
#             evens.append(i)
#     return(evens)

# n=[1,2,3,4,5,6,7,8,9]
# print(extract_even_nums(n))

# n3
# def get_neagtive_nums(a):
#     negatives=[]
#     for i in a:
#         if i<0:
#             negatives.append(i)
#     return(negatives)

# n=[-1,-3,2,4,8,-7,-4,5,21,-19]
# print(get_neagtive_nums(n))

# n4
# def filter_long_names(a):
#     long_names=[]
#     for i in a:
#         if len(i)>=5:
#             long_names.append(i)
#     return long_names

# names=["Ali", "Olim", "Murod","Shoxrux", "Javlon", "Elyor"]
# print(filter_long_names(names))

# n5
# def multiply_by_index(a):
#     lst=[]
#     for i in range(len(a)):
#         lst.append(a[i]*i)
#     return lst

# n=[1,2,3,4,5,6,7,8,9]
# print(multiply_by_index(n))

# type medium
# n6

def add_to_cart(cart: dict, product: str, price: float, quantity: int):
    cart[product]={
        'price' : price,
        'quantity': quantity
    }
    return f"{product} savatga qo'shildi"

def total_price(cart: dict):
    total=0
    for i  in cart.values():
        total+=i['price']
    return total

def remove_from_cart(cart: dict, product: str):
    for i in cart:
        if i == product:
            cart.pop(product)
            return True
        else:
            return False
cart={}
print("Mahsulot qo'shing: ")
a=True
while a:
    product=input("Mahsulot nomini kiriting: ")
    price=float(input("Mahsulot narxini kiriting: "))
    quantity=int(input("Mahsulot miqdorini kiriting: "))
    add_to_cart(cart, product, price, quantity)
    print("Savatga yana mahsulot qo'shasizmi? ")
    a=input("Y/N? ")
    if a=='Y'or a=='y':
        a=True
    elif a=="N" or a=='n':
        break

    
print(cart)
print(total_price(cart))
remove_from_cart(cart, 'Mouse')