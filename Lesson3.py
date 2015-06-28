#to comment
#when naming file, do not add spaces

#age_of_dog = 3, meaningful variable name instead of using x

names = ["corey", "philip", "rose","daniel"] #assigning variables values to varibale name in a list(need braket)
print names #without quotation to print value
print names[1] #says second name

print '\n'
for x in range(0,len(names)): #len is length of vaules, begins with 0. x signifies the integer assigned to the name
    print names[x] #indent is to inculde in for loop

print '\n'
for current_names in names: #does the same as previous example only treats names as an individual string
    print current_names
print type(current_names)

print '\n'
name=raw_input("Type your name here: ") #user inputs varibale name, raw input is used to take in answer as a string (better to not have hackers)
print "Your name is", name

print '\n'
if 1>2: #add collon for loop, only prints if true 
    print "Hello"
elif 1<2: #acts like another if, another condition. Goodbye is said because its true
    print "Goodbye"
else:
    print "I have nothing to say"
    
hello=23!=34 #!= is not equal to
print hello

#age of dog problem
print'\n'
age_of_dog=input("How old is your dog? ")
output=22+(age_of_dog -2)*5
if age_of_dog<=0:
    print "Hold on! Say whaaaaaaat"
elif age_of_dog==1: #== is equal too
    print "about 14 human years"
elif age_of_dog==2:
    print "about 22 human years"
elif age_of_dog>2: #not using else because it would fall under every other answer not previously stated (including less then 2)
    print "human years: ", output #comma to print both
    