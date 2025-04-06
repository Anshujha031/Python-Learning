# indexing = accessing e;ements of a sequence using [] (indexing operator)
 #            [start : end : step]

num = "123-158-158"

print(num[5:11])
print(num[5:])
print(num[-1])
# print(num[::2])  return the digits in 2-2 gap // 131818

last_digit = num[-4:]
print(f"xxx-xxx{last_digit}")

# print(num[::-1]) // reverse the string 