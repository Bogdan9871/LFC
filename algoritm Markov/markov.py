import re
import time


class markov:
    cuvant = ""
    vocabular = ""
    reguli = ""

    def __init__(self, cuvant):
        self.vocabular = "aba"
        self.cuvant = cuvant
        with open(
            "C:\\Users\\bogda\\Desktop\\TEME LFC\\algoritm Markov\\vocabular.txt", "r"
        ) as f:
            self.vocabular = f.readlines()  # input vocabular
            self.vocabular = "".join(self.vocabular)  # transformare intr-un string
        with open(
            "C:\\Users\\bogda\\Desktop\\TEME LFC\\algoritm Markov\\reguli.txt", "r"
        ) as f:
            self.reguli = [
                line.rstrip("\n") for line in f
            ]  # Input reguli si sterge orice whitespace sau newline

    def validate(self):  # Verificare input
        if (
            bool(all(ch in self.vocabular for ch in self.cuvant)) == True
        ):  # Verifica daca fiecare litera din vocabulare se afla in cuvant si returneaza true sau false
            return True
        else:
            return False

    def derivareMarkov(self):
        regulaDeCautat = []
        regulaDeModificat = []
        index = 0
        for regula in self.reguli:
            regulaDeModificat.append(
                re.findall("[^->]+\Z", regula)
            )  # Creare lista cu elemente de modificat

            regulaDeCautat.append(
                re.findall("^[^->]+", regula)
            )  ##Creare lista cu elemente de cautat
        regulaDeModificat = [
            s for S in regulaDeModificat for s in S
        ]  # convertire in lista simpla
        regulaDeCautat = [
            s for S in regulaDeCautat for s in S
        ]  # convertire in lista simpla
        while True:
            if self.cuvant.find(regulaDeCautat[index]) != -1:
                self.cuvant = self.cuvant.replace(
                    regulaDeCautat[index], regulaDeModificat[index], 1
                )  # first occurance
                index = 0
            else:
                index += 1
            if index == 3:
                break
            for regula in regulaDeCautat:
                if self.cuvant.find(regula) == -1:
                    break
            time.sleep(1)
            print(self.cuvant)


def startAlgorithm():

    m = markov(input("Type the word: "))
    print("Vocabularul curent: " + m.vocabular)
    if m.validate() == True:
        m.derivareMarkov()
    else:
        print("Enter a valid word!!!!")
        startAlgorithm()


while True:
    startAlgorithm()
    i = input("Do you want to try another word? (1-yes,0-no) ")
    if i == "1":
        continue
    else:
        break
