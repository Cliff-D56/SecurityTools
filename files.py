#Allows access to other files must have 'as' for methods
with open('data.txt','w') as file:
    file.write("Hello Clifford\n")
    file.write("I am Tron")

with open('data.txt','r') as file:
    data = file.read()
    print(data)