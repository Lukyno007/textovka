class Postava:
    def __init__(self, jmeno, level, exp, hp, utok, obrana):
        self.jmeno = jmeno
        self.level = level
        self.exp = exp
        self.hp = hp
        self.utok = utok
        self.obrana = obrana
        self.pouzite_zbrane = []

    def ziskat_exp(self, expy):
        self.exp += expy
        print(f"{self.jmeno} získal/a {expy} zkušeností.")

        while self.exp >= 1000:  # muzeme zmenit, kolik expu je treba na dalsi lvl
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= 1000
        self.utok += 5  # Přidáme 5 k útoku každý lvl
        self.obrana += 3  # Přidáme 3 k obraně každý lvl
        self.hp += 1 # Pridame 1 k HP za kazdy lvl
        print(f"{self.jmeno} dosáhl/a levelu {self.level}!")
        print(f"""Tve nove staty jsou: Level: {self.level}, tve zivoty jsou: {self.hp},
        tvuj utok je: {self.utok} a tva obrana je: {self.obrana}""")

    def aktualizovat_vlastnosti(self, inventar):
        for zbran in inventar.zbrane:
            if zbran not in self.pouzite_zbrane:
                self.utok += zbran.utok
                self.obrana += zbran.obrana
                self.pouzite_zbrane.append(zbran)

    def umrela_postava(self):
        if self.level >= 2:
            print("Postava umrela. Ztracis jeden lvl a znovuzrodil jsi se na stejnem miste.")
            self.level -= 1
            self.exp = 0
            self.utok -= 5
            self.obrana -= 3
            self.hp -= 1
            print(f"Tvuj lvl je: {self.level}.")
        else:
            print("Tva postava umrela. Jsi stale 1 lvl a znovuzrodil jsi se na stejnem miste.")
            self.level == 1
            self.utok == 10
            self.obrana == 5
            self.hp += (self.hp * 0) + 20 # do pice, tohle proc stale nefunguje...snad vse krat nula je vzdy nula...omg
            print(f"Tve staty jsou: utok: {self.utok}, obrana: {self.obrana} a zivot: {self.hp}.")
    def ubrat_hp(self, hpcka):
        self.hp -= hpcka
        print(f"{self.jmeno} ztratil/a {hpcka} HP.")
        if self.hp <= 0:
            self.umrela_postava()
        else:
            print(f"Stale zijes, tve zivoty jsou: {self.hp}.")
