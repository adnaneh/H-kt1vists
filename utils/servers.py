from utils.scenario import Service

class Server:
    def __init__(self, line):
        self.model = line[0]
        self.co2production = int(line[1])
        self.co2usage = int(line[2])
        self.disk = int(line[3])
        self.ram = int(line[4])
        self.cores = int(line[5])

        self.availabe_disk = self.disk
        self.availabe_ram = self.ram
        self.availabe_core = self.cores

        self.running_services = []

    def impact_co2(self, nb_annee=0):
        return self.co2production + self.co2usage * nb_annee

    def can_add_service(self, service: Service):
        if service.nb_proc > self.availabe_core or service.volume_ram > self.availabe_ram or service.volume_stockage > self.availabe_disk:
            return False
        return True

    def add_service(self, service: Service):
        self.availabe_disk -= service.volume_stockage
        self.availabe_core -= service.nb_proc
        self.availabe_ram -= service.volume_ram
        self.running_services.append(service)

    def clone(self):
        return Server([self.model, self.co2production, self.co2usage, self.disk, self.ram, self.cores])
    