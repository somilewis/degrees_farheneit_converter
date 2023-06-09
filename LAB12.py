
# Lewis Muthomi
# 1250 01
# Lab 12
# 11/13/2022


# User Greeting
def greeting():
    print('This program will convert degrees Celsius to degrees Fahrenheit.')
    print('Please enter the temperature in degrees Celsius; you may use decimals.')
    print()

# Ask if run again and error check
def runAgain():
    again = input('Would you like to run the program again?(y/n): ').lower()

    while again != 'y' and again != 'n':
        again = input('INPUT ERROR: Please type a y or n: ').lower()
        
    if again == 'y':
        run = True
    else:
        run = False
            
    return run

#--------------------Main---------------------------
# user greeting
greeting()

# init runProgram
runProgram = True

# start program loop
while runProgram == True:

    # get user input
    temp = input('Enter a temperature in degrees Celsius: ') 

    # do the calculations
    answer = (float(temp) * 9/5) + 32

    # Display and format results
    print(temp + ' degrees Celsius is equal to ' + str(answer) + ' degrees Fahrenheit')
    print()

    # call the runAgain function
    runProgram = runAgain()

# exit message
print()
print('Have a nice day!!!!!!!')
