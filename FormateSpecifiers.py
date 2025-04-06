# format specifiers = {value:flag} format a value based on what flags are inserted
#  
#  .(number)f = round to that many decimel places (fixed point)
#  :(number)  = allocate that many spaces
#  :03 = allocate and zero pad that many spaces
#  :< = left justify
#  :> = right justify
#  :^ = center align
#  :+ = use a plus sign to indicate positive value
#  : = insert a space before positive number
#  := = place sign to leftmost positive
#  :, = comma separator (thousand separted)         

price1 = 3.14159
price2 = -987154.654
price3 = 12.34

print(f"Price 1 is {price1:+,.2f}")
print(f"Price 2 is {price2:+,.2f}") 
print(f"Price 3 is {price3:}")