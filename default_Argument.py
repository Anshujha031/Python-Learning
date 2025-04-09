# default arguments = A default value for certain parameters
#                     default is used when that argument is ommitted
#                     make your functions more flexible, reduces no of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitary


# import time

# def count(end,start =0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")

# count(10)


#========================================================================
# keyword arguments = an argument preceeded by an identifier
#                      helps with readability
#                      order of arguments doesn't matter
#                      1. positional 2. default 3, KEYWORD 4. arbitary
'''
def hello(greeting , first , last):
    print(f"{greeting} {first} {last}")

hello("Hello" , first="Naveen" , last="Jha") # here the positional agrument comes first than keyword

for x in range(1,10):
    print(x , end=" ") # here end=" " is an keyword argument that print an space
'''

#==============================================================================
#*args = allows you to pass multiple non-key arguments by default type is tuple
#**kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#             4. ARBITRARY

'''
def add(*args):
    total =0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4))
'''

'''
def print_adderss(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

print_adderss(street="123 fake st",city="india",state="mp")
'''

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")

shipping_label("Dr","spongbob","IIt",street="100",apt="detroit")
