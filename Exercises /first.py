#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that 
#they will turn 100 years old. 

#This excercise helps learners to use:
#   variables, 
#   accept input from console
#   import the datetime module, 
#   Use the datetime function

import datetime


name = input("What is your name:")

#convert the age input from string (default) to integer vaue - 
# No other checks are done as this is basic level of programming 
age = int(input("How old are you:"))

#here we will use the today function from teh datetime module date class
#onece we get the day of today, we will extract the current yeat
#We will subtract the age of the person from current year to get he birth year
today_year = datetime.date.today().year
birth_year = (today_year - age)
year_100 =  birth_year + 100


print(name, ",you will be 100 years old in ", year_100)


#This is just one example of computing the poblem. There can be other methods