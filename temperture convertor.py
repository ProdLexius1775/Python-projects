

#convert fahrenheit to celius

#list or based tempertures <90 degress and up: red> <75  - 89 degrees: yellow> <64 -74 degrees: green> <63 and below: blue>


#print temperture in both fahrenhiet and celsius, print in the color assigned to the to the temperture
#User input to take in temperture



#Format Celsius to show only one place after the decimal
#i.e.,  22.8888888888 --> 22.8



import random
from colorama import Fore

red = Fore.RED
black = Fore.BLACK
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE

def tempertureConverter(user_input):
    FAHRENHEIT_TO_CELSIUS = (user_input - 32) * 5/9

    if(user_input >= 90):
        print("fahrenheit  :", red, user_input, black)
        print("Celsius: ", red, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS), black)
    elif(user_input >= 75) & (user_input <= 89):
        print("Fahrenhiet: ", yellow, user_input, black )
        print("Celeius: ", yellow, "{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS),black)
    elif(user_input >= 64) & (user_input) <= 74:
        print("Fahrenheit  :", green, user_input, black)
        print("Celsius: ", green,"{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS) , black)
    else:
        print("Fahrenheit  :",blue , user_input, black)
        print("Celsius: ", blue ,"{0:4.1f}".format(FAHRENHEIT_TO_CELSIUS) , black)

user=float(input("Enter a temperture in Fahrenhiet to convert to Celsius ") )

for x in range(5):
    tempertureConverter(user)
    user=float(input("Enter a temperture in Fahrenheit to convert to Celsius: ") )