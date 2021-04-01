class Server:
    def __init__(self, line):
        self.model = line[0]
        self.co2production = line[1]
        self.co2usage = line[2]
        self.disk = line[3]
        self.ram = line[4]
        self.cores = line[5]