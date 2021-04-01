class Service:
    def __init__(self, line):
        self.nom = line[0]
        self.volume_stockage = line[1]
        self.volume_ram = line[2]
        self.nb_proc = line[3]

class Scenario:
    def __init__(self, csv_reader):
        self.nb_annees = 0
        self.services = []

        for idx, line in enumerate(csv_reader):
            if idx == 0:
                self.nb_annees = int(line)
            else:
                self.services.append(Service(line))