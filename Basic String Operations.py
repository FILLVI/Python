astring = "Hello world!"
print(astring[3:7])

##################

print(astring[3:7:2])

##################

print(astring[3:7])
print(astring[3:7:1])

#####################

print(astring[::-1])

######################

print(astring.upper())
print(astring.lower())

#####################

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#####################

afewwords = astring.split(" ")

###############################

s = "Het there! what should this string be?"

#Lenght should be 20
print("Lenght of s = %d" % len(s))

#First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

#Number of a's should be 2
print("a occurs %d times" % s.count("a"))

#Slicinh the string into bits
print("The first five characters are '%s'" %s[:5])#Start to 5
print("The next five characters are '%s'" %s[5:10])# 5 to 10
print("The thirteenth characters is '%s'" %s[12])#Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" %s[-5:])#5th-from-last to end

#Convert everything to uppercase
print("String in uppercase: %s" %s.upper())

#Convert everything in lowcase
print("String in lowercase: %s" %s.lower())

#Check how a string starts
if s.startswith("Str"):
    print("String stats with 'Str'. Good!")

    #Check how a string end
    if s.endswith("ome!"):
        print("String end with 'ome'. Good!")

#Split the string into there separate strings,
#each containing only a word

print("Split the words of the string: %s" %s.split(" "))