gender = "f"

###########CONDITIONALS
if gender == 'f':
    print "welcome to hear me code"
#### mus have had a tab after semicolon in the if statement

students = 10
capacity = 30

if students < capacity:
    print "keep recruiting"
else:
    print "end ticket signups"

tas = 6
if tas == 0:
    print "uh oh!"
elif tas < students/5:
    print "keep recruiting TA's"
else:
    print "aren't the TAs awesome?"
    

volunteers = 100
goal = 110
diff = abs(volunteers - goal)

if volunteers == goal:
    print "met goal"
elif volunteers < goal:
    print "below goal by {0}".format(diff)
else:
    print "above goal by {0}".format(diff)
 
### could have used print "{0} volunteers over the goal".format(volunteers-goal)

##########COMPOUND conditionals
##### if volunteers ==0 and or




