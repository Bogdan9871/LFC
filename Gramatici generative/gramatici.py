class gramatica:  # G=(VN, VT,S,P)
    vn = ""
    vt = ""
    simbolStart = ""
    productie = ""
    numar = int()

    def __init__(self):
        with open(
            "C:\\Users\\bogda\\Desktop\TEME LFC\\Gramatici generative\\VN.txt", "r"
        ) as f:
            self.vn = f.readlines()
            self.vn = "".join(self.vn)  # transformare in string
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

    def print(self):
        print("G=(", self.vn, self.vt, self.simbolStart, ",P)")
        print("P= ", self.productie)


def startAlgorithm():
    g = gramatica()
    g.print()


startAlgorithm()
