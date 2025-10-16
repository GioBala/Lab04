class Passeggero:
    def __init__(self, codice_passeggero, nome,cognome):
        self.codice= codice_passeggero
        self.nome = nome
        self.cognome = cognome
        self.camera = ""

    def modifica_camera(self,camera):
        self.camera = camera

    def __str__(self):
        if self.camera == "":
            c="Nessuna"
        else:
            c=self.camera
        return f'Codice passeggero: {self.codice}, Nome: {self.nome}, Cognome: {self.cognome}, Camera: {c}'