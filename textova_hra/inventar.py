# inventar.py

class Inventar:
    def __init__(self):
        self.zbrane = []

    def pridat_zbran(self, zbran):
        self.zbrane.append(zbran)

    def odebrat_zbran(self, zbran):
        if zbran in self.zbrane:
            self.zbrane.remove(zbran)
            print(f"{zbran.jmeno} bylo odebráno z inventáře.")
        else:
            print(f"{zbran.jmeno} není v inventáři.")

    def vypis_inventar(self):
        if not self.zbrane:
            print("Inventář je prázdný.")
        else:
            print("Obsah inventáře:")
            for zbran in self.zbrane:
                print(f"Jméno: {zbran.jmeno}, Útok: {zbran.utok}, Obrana: {zbran.obrana}")

