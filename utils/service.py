class Service:
    def __init__(self, line):
        self.nom = line[0]
        self.volume_stockage = int(line[1])
        self.volume_ram = int(line[2])
        self.nb_proc = int(line[3])