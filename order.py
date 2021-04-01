import csv
from utils.servers import Server
from utils.scenario import Scenario
from utils.score import *
from tqdm import tqdm

input_number = "4"

server_catalog = "codecontest_fr_df_accenturehackathome/servers_catalog.csv"
scenario_file = "ctstfr0280_input_" + input_number + ".csv"

catalog = []
scenario = None

# Loading server catalog
with open(server_catalog, "r") as server_file:
    reader = csv.reader(server_file, delimiter=',')
    for idx, row in enumerate(reader):
        if idx != 0:
            catalog.append(Server(row))

# Loading scenario
with open(scenario_file, "r") as scenario_file:
    reader = csv.reader(scenario_file, delimiter=',')
    scenario = Scenario(reader)

# sort server by lowest impact for current scenario
catalog = sorted(catalog, key=lambda server: server.impact_co2(scenario.nb_annees))

## -------------------------

servers = []
while len(scenario.services) > 0:
    biggest = max(scenario.services)
    scenario.services.remove(biggest)

    for s in servers:
        if s.can_add_service(biggest):
            s.add_service(biggest)
            break
    else:
        for s in catalog:
            if s.can_add_service(biggest):
                new_s = s.clone()
                new_s.add_service(biggest)
                servers.append(new_s)
                break

print("Score: ", calcule_score(scenario, servers))
solution = produire_solution(servers)
print("Solution: \n" + solution)

res_to_file("input_" + input_number + ".csv", solution)