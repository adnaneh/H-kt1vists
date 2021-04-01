class Service:
    def __init__(self, line):
        self.nom = line[0]
        self.volume_stockage = int(line[1])
        self.volume_ram = int(line[2])
        self.nb_proc = int(line[3])

    def __ge__(self, other):
        if self.nb_proc >= other.nb_proc:
            return True
        if self.volume_ram >= other.volume_ram:
            return True
        if self.volume_stockage >= other.volume_stockage:
            return True
        return False

    def __gt__(self, other):
        if self.nb_proc > other.nb_proc:
            return True
        elif self.nb_proc == other.nb_proc:
            if self.volume_ram > other.volume_ram:
                return True
            elif self.volume_ram == other.volume_ram:
                if self.volume_stockage > other.volume_stockage:
                    return True

        return False

    def __add__(self, other):
        return Service([
            "",
            self.volume_stockage + other.volume_stockage,
            self.volume_ram + other.volume_ram,
            self.nb_proc + other.nb_proc
            ])

    def __repr__(self):
        return f"Service: CPU: {self.nb_proc}, RAM: {self.volume_ram}, Disk: {self.volume_stockage}"