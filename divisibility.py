#LARIS NDAMO
#PROJECT 2: DIVISIBILITY
#MATH-220
#GOAL: In this project, you will be using Excel (or the program of your choice) to develop a program to take a number in and determine if it is divisible by 2, 3, 4, 5, 6, 7, 8, 9, 10, and 11.
#The program should request a natural number that is between 1 and 6 digits in length (and not zero).
#The program should fail and re-ask for a natural number of the appropriate number of digits if more than 6 digits are entered, if “0” is entered, if a negative is entered, or if a decimal is entered
  
#Method to print divisibility
def divisibility(num):
  newNum = int(num)
  for i in range(2,12):
    if newNum % i == 0:
      print(f"The number is divisible by {i}")
    else:
      print(f"The number is not divisible by {i}")
      

#Method to Validate input
def validation(num):
  if num.isnumeric() == True and num.isdecimal() == True: #Checking conditions
        newNum = int(num)
        if len(num) > 6 or newNum == 0 or newNum < 0:
            num = input("Please enter a valid number \n(Between 1 to 6 digits, and not zero): ")
            validation(num)#Recall the method till valid input is entered
  elif num.isnumeric() == False: #Check if the input has something other than numbers
         num = input("Please enter a valid number \n(Must be a number between 1 to 6 digits, and not zero): ")
         validation(num)

  
#Running the code....
         
#Get input
num = input("Please enter a number: ")
validation(num)
divisibility(num)
