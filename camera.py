class Camera:
    def __init__(self,codice,letti,ponte,prezzo):
        self.codice = codice
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo
        self.passeggero= ""

    def modifica_passeggero(self, passeggero):
        self.passeggero = passeggero

    def __str__(self):
        if self.passeggero == "":
            c="Disponibile"
        else:
            c="Non disponibile"

        return f'{self.codice}: Normale | {self.letti} letti - Ponte: {self.ponte} - {c}\n'



class Camera_deluxe(Camera):
    def __init__(self, codice,letti,ponte,prezzo,tipo):
        super().__init__(codice, letti, ponte, prezzo)
        self.tipo=tipo
        self.prezzo = prezzo * 1.20

    def __str__(self):
        if self.passeggero == "":
            c="Disponibile"
        else:
            c="Non disponibile"

        return f'{self.codice}: Deluxe - {self.tipo} | {self.letti} letti - Ponte: {self.ponte} - {c}\n'


class Camera_animali(Camera):
    def __init__(self, codice,letti,ponte,prezzo,num_animali):
        super().__init__(codice, letti, ponte, prezzo)
        self.num_animali = num_animali
        self.prezzo = prezzo * (1 + 0.10 * num_animali)

    def __str__(self):
        if self.passeggero == "":
            c="Disponibile"
        else:
            c="Non disponibile"

        return f'{self.codice}: Animali | {self.letti} letti - Ponte: {self.ponte} - Max animali: {self.num_animali} - {c}\n'

