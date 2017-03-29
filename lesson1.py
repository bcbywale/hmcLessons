#########USING PRINT FUNCTION
print "watch out world!"

###########VARIABLES
twitter = "@hearmecode"
members = 901
print twitter
print "my governor's name is Martin O'Malley"

###########PRINTING WITH QUOTES
# print 'my governor's name is Martin O'Malley' this didn't work
# use a """ and end with """ if you have a really long string, sometimes coping things from website doesn't work
# backslash is by the backspace!

###########TABS AND NEW LINES
print "Contact info:\t Shannon\nPhone:\t\t 123-4566-789"
print "Lesson\t Topic \n1\t Strings and Conditionals"
print "2\t Lists and Loops"
print "3\t Dictionaries and Files"
print "length of twitter variable"

###########USING LEN FUNCTION
print len(twitter)
#python starts counting at 0 

###########SLICING
print twitter[1:5]
phone = "(202) 456-7890"
print phone[1:4], "hi"
print phone[6:9]

###########FORMATING, USE THE {} BRACKETS!

name = "Lili"
age = 29
print "my name is {0} and my age is {1}".format(name,age)
print "my name is {0} and my age is {1}".format(name[:1],age)
print "my name is {0} and my age is {1}".format(name[:1],age+1)

print "area code:{0}".format(phone[1:4])
print "local:{0}".format(phone[6:])
print "phone number:{}".format(phone)

###########STRINGS METHODS .FIND IS SORT OF LIKE CTLR +F
email = "suellen.foth@gmail.com"
print email.find("@")

print twitter.replace("@","#")
print twitter
# doesn't save the changes, we need to redefine the twitter variable
twitter = twitter.replace("@","#")
print twitter


length = len(twitter)
print length

position = twitter.find("#")
print position

address = '        1600 Pennslyvania Avenue'
print address
print address.strip()


gender = "f"
print gender
print gender.lower()
print gender.upper()
gender = gender.upper()

print gender
sentence = "try to count how many times z is in this string"
print sentence.count("z")

###########CONDITIONALS
if gender == 'f'
print "welcome to hear me code"















