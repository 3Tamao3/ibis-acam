print("**************************")
print("*        Rene Özbay      *")
print("*        Temparatur      *")
print("*         App17b         *")
print("**************************")

auswahl = input("Was möchten sie umrechnen (Temparatur = t, Energie Einheiten = e): ")

if (auswahl == "t"):
    userInput = input("Was möchten sie umrechnen (Celcius = c, Kelvin = k, Fahrenheit = f): ")
    userInputInt = int(input("Geben Sie die Zahl ein die sie umrechnen möchten: "))

    if (userInput == "c"):
        print(userInputInt * 9 / 5 + 32)
        print(userInputInt + 273.15)
    elif (userInput == "k"):
        print(userInputInt - 273.15)
        print((userInputInt - 273.15) * 9 / 5 + 32)
    elif (userInput == "f"):
        print((userInputInt - 32) * 5 / 9)
        print((userInputInt - 32) * 5 / 9 + 273.15)
    else:
        print("Invalid Input")
elif (auswahl == "e"):
    userInputInt = int(input("Gib eine Zahl in Joule ein die du umrechnen möchtest: "))

    print("Cal.: ", userInputInt / 4.1868)
    print("eV.: ", userInputInt / 16.022)
    print("kWh.: ", userInputInt / 3.6)
    print("Btu.: ", userInputInt / 1055.1)

else:
    print("Invalid Input")
