import csv
from camera import Camera, Camera_animali, Camera_deluxe
from passeggero import Passeggero

class Crociera:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.nome=nome
        self.passeggeri=[]
        self.camere=[]

    """Aggiungere setter e getter se necessari"""
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        with open(file_path, newline='') as file:
            lettore = csv.reader(file)
            for riga in lettore:
                #print(len(riga))
                if len(riga) == 3:
                    self.passeggeri.append(Passeggero(riga[0], riga[1], riga[2]))
                elif len(riga) == 4:
                    self.camere.append(Camera(riga[0], riga[1], riga[2], riga[3]))
                elif len(riga) == 5 and riga[4].isdigit():
                    self.camere.append(Camera_animali(riga[0], riga[1], riga[2], riga[3], riga[4]))
                else:
                    self.camere.append(Camera_deluxe(riga[0], riga[1], riga[2], riga[3], riga[4]))



    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        for c in self.camere:
            if c.codice == codice_cabina and c.passeggero == "":
                for p in self.passeggeri:
                    if p.codice == codice_passeggero and p.camera == "":
                        c.modifica_passeggero(codice_passeggero)
                        p.modifica_camera(codice_cabina)
                        return None
        raise Exception("Cabina o passeggero non validi")



    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabine_ordinate= sorted(self.camere, key=lambda c: c.prezzo)
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for p in self.passeggeri:
            print(p)


