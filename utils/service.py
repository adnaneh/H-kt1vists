class Service:
    def __init__(self, line):
        self.nom = line[0]
        self.volume_stockage = line[1]
        self.volume_ram = line[2]
        self.nb_proc = line[3]