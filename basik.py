name = "Clifford" #This is a string
age = 28 #This is an int
List = ["Wrath","Edward","Rahim"] #This is a list
dictionary = { #This is a Dictionary
    "Security":"CliffordOS",
    "Admin":"Clifford"
}

#Functions and Error Handling
def returnInput():
    try:
        return input("Type in Your name: ")
    except KeyboardInterrupt:
        print("\nYou used Control C and cancelled operation")
     

    
#If Statements
if name == "Clifford":
    print("You suck")
elif name == "Anna":
    print("Im upset with you")
else:
    print("You aint special")
List.append(name)

#Loops
for index,item in enumerate(List, start=1):
    print(f"{index} {item} Gardner")
print(name +  " aint your name, your name is Shithead!!!")
print(List)

name2 = returnInput()
while name2 == "":
    name2 = returnInput()

print(f"Hello {name2}") 

