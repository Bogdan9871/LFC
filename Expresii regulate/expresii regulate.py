# 1. 2p - Să se verifice dacă un string dat este sau nu este număr întreg sau număr real.
import re


def firstExercise():
    numar = input("Introduceti numarul: ")

    def verificare(arg):

        if re.search("[.]", arg):
            print("Numarul este real")
        else:
            print("Numarul este intreg")

    verificare(numar)

    # 3. 4p - Se dă o parolă. Să se verifice dacă aceasta este strong sau nu. O parolă este strong


def secondExercise():
    cuvinte = open(
        "C:\\Users\\bogda\\Desktop\\TEME LFC\\Expresii regulate\\cuvinte.txt", "r"
    ).read()
    parCounter = int()
    cuvinteList = []
    for word in cuvinte.split():
        cuvinteList.append(word)
    for word in cuvinteList:
        for char in word:
            if char == "a":
                parCounter += 1

    print(cuvinteList, parCounter)


def thirdExercise():
    parola = input("Introducet parola: ")

    def verificarePassword(passwd=""):
        if (
            bool(re.search("[!@#$%^&*]\Z", passwd))
            == True  # Verificare carctere speciale
            and bool(re.search("[A-Z]", passwd)) == True  # Verificare carctere upper
            and bool(re.search("[0-9]{2}", passwd))
            == True  # Verificare daca sunt 2 cifre una langa alta
            and len(passwd) > 10
        ):

            print("Password is Strong")
        else:
            print("Pasword is not strong.")
            thirdExercise()

    verificarePassword(parola)


# while True:
#     if (
#         input(
#             "Select option: \n"
#             + "1. Check if number is integer or double \n"
#             + "3.Check if password is strong \n"
#         )
#         == "1"
#     ):
#         firstExercise()
#     else:
#         thirdExercise()
#     if input("Select another option? (1-yes,0-no): ") != "1":
#         break
secondExercise()
