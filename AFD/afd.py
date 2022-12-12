class afd:
    stari = ""  # Q
    sigma = ""
    delta = ""
    stariInitiale = "q0"
    stariFinale = ""
    cuvant = ""

    def __init__(self):
        with open("C:\\Users\\bogda\Desktop\\TEME LFC\\AFD\\Sigma.txt", "r") as f:
            self.sigma = [line.rstrip("\n") for line in f]  # transformare in string
        with open("C:\\Users\\bogda\Desktop\\TEME LFC\\AFD\\Delta.txt", "r") as f:
            self.delta = [line.rstrip("\n") for line in f]  # transformare in string
        with open("C:\\Users\\bogda\Desktop\\TEME LFC\\AFD\\Finale.txt", "r") as f:
            self.stariFinale = [
                line.rstrip("\n") for line in f
            ]  # transformare in string
        with open("C:\\Users\\bogda\Desktop\\TEME LFC\\AFD\\Stari.txt", "r") as f:
            self.stari = [line.rstrip("\n") for line in f]  # transformare in string

    def citire(self):
        self.cuvant = input("Introduceti Cuvantul: ")

    def validare(self):
        flag = False
        for i in range(len(self.stari)):  # Prima conditie
            for j in range(len(self.stari)):
                if i != j:
                    if self.stari[i] == self.stari[j]:
                        flag = True
        if flag == True:
            print("Elementele starilor nu sunt unice")
        else:
            print("Elementele starilor sunt unice")
        if all(x in self.sigma for x in self.cuvant):
            print("Cuvantul introdus este format din vocabularul dat")
        else:
            print("Cuvantul introdus nu este format din vocabularul dat")

        if (self.stariInitiale in self.stari) == True:
            print("q0 este din Q")
        else:
            print("q0 nu se afla in Q")
        if set(self.stariFinale).issubset(set(self.stari)) == True:
            print("F este inclus in Q")
        else:
            print("F nu este inclus in Q")

    def afisare(self):
        print("Automatul finit de forma| M=(Q,Σ,δ,q0,F)")
        print(
            "Unde:" + "\n" + "Q=",
            self.stari,
            "\n",
            "Σ=",
            self.sigma,
            "\n",
            "δ=",
            self.delta,
            "\n",
            "F=",
            self.stariFinale,
        )


Afd = afd()
Afd.citire()
Afd.afisare()
Afd.validare()
