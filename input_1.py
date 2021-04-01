import csv
from utils.servers import Server
from utils.scenario import Scenario

server_catalog = "codecontest_fr_df_accenturehackathome/servers_catalog.csv"
scenario_file = "ctstfr0280_input_1.csv"

servers = []
scenario = None

# Loading server catalog
with open(server_catalog, "r") as server_file:
    reader = csv.reader(server_file, delimiter=',')
    for row in reader:
        servers.append(Server(row))

# Loading scenario
with open(scenario_file, "r") as scenario_file:
    reader = csv.reader(scenario_file, delimiter=',')
    scenario = Scenario(reader)