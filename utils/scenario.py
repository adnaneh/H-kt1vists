from utils.service import Service

class Scenario:
    def __init__(self, csv_reader):
        self.nb_annees = 0
        self.services = []

        for idx, line in enumerate(csv_reader):
            if idx == 0:
                self.nb_annees = int(line[0])
            else:
                self.services.append(Service(line))