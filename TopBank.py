#I will import time to slow down the code so that everything doesn't go at once
import time
#I will import system to allow the code to end
import sys
#I will welcome the user to the bank
print("**Welcome to TopBank**")
#I will create variables to store my first and last name
name1 = "Linus"
name2 = "Brownlee"
#I will create a variable called al which means attempts left
al = 3
#I will ask the user to input their first name
name3 = input("Please enter your first name: ")
#I will create a 1 second pause
time.sleep(0)
#I will now ask the user to input their first name
name4 = input("Please enter your surname: ")
#I will create a while loop
while name3 != name1 or name4 != name2:
  #I will take away an attempt
  al = al - 1
  #I will create an if statement to see if the user has used up all their tries
  if al != 0:
    #I will print out that the name inputted is incorrect
    print("We are sorry, but the name you inputted is incorrect. Please try again.")
    #I will redo the input name in this if statement inside a while loop to loop it if they get it wrong
    name3 = input("Please enter your first name: ")
    time.sleep(0)
    name4 = input("Please enter yout surname: ")
  #I will create the else statement incase the user inputs an incorrect name
  else:
    print("You have inputted too many incorrect names")
    time.sleep(1)
    print("This card will no longer work if you try to use it")
    #I will now stop the system
    sys.exit(0)
#I will now ask the user to enter their date of birth, or DOB
DOB = input("Please enter your Date of Birth in the DD/MM/YYYY format: ")
#I will create a date attempts variable
dl = 3
#I will now create an while loop to make sure the date entered is correct
while len(DOB) != 10 or DOB[2] != "/" or DOB[5] != "/":
  print("You have done an error in writing your Date of Birth. Either add a / after your day and month or add a 0 to single digit dates.")
  dl = dl - 1
  #I will now create an if statement
  if dl != 0:
    DOB = input("Please enter your Date of Birth in the DD/MM/YYYY format: ")
  else:
    print("It seems as if you have ran out of attemps!")
    time.sleep(0.5)
    print("This card will no longer work")
    time.sleep(0.5)
#I will create a variable to store their password
password = name2 + DOB[3]+DOB[4]+DOB[8]+DOB[9]
print("Hello "+name1+" "+name2+", your password is "+password)
#I will create a variable to see their account
balance = 1000
inflation = 110
print("Your current balance is £"+str(balance))
time.sleep(0.5)
#I will ask the user to input how much they want inputted
intput = int(input("How much money do you want inputted into your account?: "))
#I will now create a while loop 
while intput > 100000:
  print("You have input an amount which is too large.")
  time.sleep(1)
  intput = int(input("Please enter an amount lower than 100,000: "))
balance = balance + intput
print("Your new account balance is "+str(balance))
#I will now multiply the account balance by 110%
balance = (int(balance) * int(inflation))/100
print("Your account balance next week will be £"+str(balance))