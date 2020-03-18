class Sudoku:
    """
    Predstavlja mrežo za posamezen sudoku
    """
    def __init__(self, mreza):
        self.mreza = mreza
        self.velikost = len(self.mreza)
        self.mala_velikost = round(self.velikost ** 0.5)

    def lep_izpis(self):
        """
        Vrne niz, ki vsebuje lepo izpisan sudoku
        """
        celota = ""

        for st_vrstice in range(self.velikost):
            vrstica = self.mreza[st_vrstice]
            trenutna = ""
            if st_vrstice % self.mala_velikost == 0:
                for manjsa_celica in range(self.mala_velikost):
                    trenutna += "+" + ("-"*self.mala_velikost)
                trenutna += "+\n" # Gremo v novo vrstico
            for st_stolpca in range(self.velikost):
                if st_stolpca % self.mala_velikost == 0:
                    trenutna += "|"
                znak = vrstica[st_stolpca]
                trenutna += str(znak)
            trenutna += "|"
            # Zadnji vrstici ne dodam nove vrstice
            if not (st_vrstice == self.velikost - 1):
                trenutna += "\n"
            celota = celota + trenutna
        celota += "\n"
        for manjsa_celica in range(self.mala_velikost):
            celota += "+" + ("-"*self.mala_velikost)
        celota += "+" # Ne gremo v novo vrstico
        return celota

    def ima_veljavne_vrstice(self):
        pass

    def ima_veljavne_stolpce(self):
        pass

    def ima_veljavne_kvadratke(self):
        pass

    def je_veljaven(self):
        pass


def preberi_datoteko(ime_datoteke):
    """
    Funkcija prebere in vrne sudoku 
    iz podane datoteke
    """
    datoteka = open(ime_datoteke, "r")
    prebrano = []
    for vrstica in datoteka:
        vrstica = vrstica.strip()
        vr_stevilke = []
        
        for znak in vrstica:
            vr_stevilke.append(int(znak))

        prebrano.append(vr_stevilke)
    return Sudoku(prebrano)

sudoku = preberi_datoteko(
    "sudoku/sudoku.in"
)

print(sudoku.lep_izpis())


