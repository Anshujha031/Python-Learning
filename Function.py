# fuction = A block of reuable code
#           place () after the function name to invoke it

# def happy_birth(name,age):
#     print(f"hppy birth day {name}")
#     print(f"you are {age} years old")

# happy_birth("Bro" , 20)

# def display_invoice(username,amount,due_date):
#     print(f"user:{username}") 
#     print(f"Your bill of ${amount} is due: {due_date}")

#-------------------------------------------------
# return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x+y
    return z

print(add(2,3))