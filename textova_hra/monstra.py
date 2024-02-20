class Monstra:
    def __init__(self, jmeno, utok, obrana, zivot):
        self.jmeno = jmeno
        self.utok = utok
        self.obrana = obrana
        self.zivot = zivot

    def ubrat_zivot(self, zivoty):
        self.zivot -= zivoty
        print(f"{self.jmeno} ztratil/a {zivoty} HP.")
        if basilisek.zivot >= 0:
            print(f"Haha, stale ziju !!! Basilisek ma: {self.zivot} zivota. ")

        else:
            basilisek.monster_umrel()

    def monster_umrel(self):
        print("Basilisek umrel.")





basilisek = Monstra("Bazilišek", 10, 7, 25)
bohuta = Monstra("Nasranej Bohuta", 40, 25, 30)



