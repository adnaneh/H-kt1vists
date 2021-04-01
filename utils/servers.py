class Server:
    def __init__(self, line):
        self.model = line[0]
        self.co2production = int(line[1])
        self.co2usage = int(line[2])
        self.disk = int(line[3])
        self.ram = int(line[4])
        self.cores = int(line[5])