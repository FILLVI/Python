x = 2
print(x == 2)#prints out True
print(x == 3)#print out False
print(x<3)#prints out True

#################
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

###################

if name in ["John","Rick"]:
    print("Your name is either John or Rick.")

######################

#if <statement is ="" true="">:
   # <do something="">
    # .......
#elif <another statement="" is="" true="">:#else if
    #<do something="" else="">
   # .....
   # .....
#else:
    #<do another="" thing="">
    #......
    #......
#</do></do></another></do></statement>

x = 2
if x==2:
    print("x quals two!")
else:
    print("x does not equal to two.")

###################
x = [1,2,3]
y = [1,2,3]
print(x == y)#Print out True
print(x is y)# Prints out of False

##################

print(not False)#Prints out True
print((not False) == (False))#Prints out False

###################

#change this code
number = 26
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

    if not second_number:
        print("6")