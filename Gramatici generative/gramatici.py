import re


class gramatica:  # G=(VN, VT,S,P)
    vn = ""
    vt = ""
    simbolStart = ""
    productie = ""
    numar = int()
    productieDreapta = []
    productieStanga = []

    def __init__(self):
        with open(
            "C:\\Users\\bogda\\Desktop\TEME LFC\\Gramatici generative\\VN.txt", "r"
        ) as f:
            self.vn = [line.rstrip("\n") for line in f]  # transformare in string
        with open(
            "C:\\Users\\bogda\\Desktop\\TEME LFC\\Gramatici generative\\VT.txt", "r"
        ) as f:
            self.vt = [line.rstrip("\n") for line in f]  # stergere newspace

        with open(
            "C:\\Users\\bogda\\Desktop\\TEME LFC\\Gramatici generative\\simbolStart.txt",
            "r",
        ) as f:
            self.simbolStart = f.readlines()
            self.simbolStart = "".join(self.simbolStart)

        with open(
            "C:\\Users\\bogda\\Desktop\\TEME LFC\\Gramatici generative\\productii.txt",
            "r",
        ) as f:
            self.productie = [line.rstrip("\n") for line in f]
        for productie in self.productie:
            self.productieDreapta.append(
                re.findall("[^->]+\Z", productie)
            )  # Creare lista cu elemente de modificat

            self.productieStanga.append(
                re.findall("^[^->]+", productie)
            )  ##Creare lista cu elemente de cautat
        self.productieStanga = [
            s for S in self.productieStanga for s in S
        ]  # convertire in lista simpla
        self.productieDreapta = [s for S in self.productieDreapta for s in S]

    def print(self):
        print("G=(", self.vn, self.vt, self.simbolStart, ",P)")
        print("P= ")
        for ind in range(len(self.productie)):
            print("(", ind, ")", self.productie[ind])

    def verificare(self):

        if bool(set(self.vn) & set(self.vt)) == True:  # verifica intersectia
            print("Prima conditie nu este indeplinita")
        else:
            print("Prima conditie este indeplinita")
        if (self.simbolStart in self.vn) == True:
            print("A doua conditie este indeplinita")
        else:
            print("A doua conditie nu este indeplinita")
        if all(ch in self.vn for ch in self.productieStanga):
            print("A treia conditie este indeplinita")
        else:
            print("A treia conditie nu este indeplinita")
        if ("S" in self.productieStanga) == True:
            print("A patra condtie este indeplinita")
        else:
            print("A patra condtie nu este indeplinita")

        if all(ch in self.vn for ch in self.productieStanga) == True:
            print("A cincea condtie este indeplinita")
        else:
            print("A cincea conditie nu este indeplinita")


def startAlgorithm():
    g = gramatica()
    g.verificare()
    g.print()


startAlgorithm()
