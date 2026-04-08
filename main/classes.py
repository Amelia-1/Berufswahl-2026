#defines all classes

class Schüler:
    def __init__(self, vorname, nachname, klasse, wahl1, wahl2):
        self.vorname = vorname
        self.nachname = nachname
        self.name = nachname + vorname
        self.klasse = klasse
        self.wahl = wahl1.split(", ") + wahl2.split(", ")

    def debug_print(self):
        for i,v in vars(self).items():
            print(v)

a = Schüler("Horst", "Müller" , "8b", "eins, zwei, drei", "vier")

print(a.wahl)