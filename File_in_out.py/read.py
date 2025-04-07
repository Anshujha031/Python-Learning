# Reading a file
'''
f = open("myFile.txt","r")

text = f.read()
print(text)
f.close()
'''


# writting file
'''
f = open("myFile2.txt","w")
f.write("Hello, World!")
f.close()


with open("myFile.txt",'a') as f:
    f.write("hey i am inside that!")
    '''

# readlinea() method
f = open("myFile.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)