import csv
from utils.servers import Server
from utils.scenario import Scenario
from utils.score import *
from tqdm import tqdm

input_number = "3"

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
catalog = sorted(catalog, key=lambda server: server.impact_co2(scenario.nb_annees), reverse=True)

## -------------------------

servers = []
while len(scenario.services) > 0:
    # on trie les serveurs par place restante
    servers = sorted(servers, reverse=True)

    # on prend le plus gros service
    biggest = max(scenario.services)
    scenario.services.remove(biggest)

    can_add = False
    for s in servers:
        if s.can_add_service(biggest):
            can_add = True
            s.add_service(biggest)
            break
        
    if not can_add:
        found = False
        for cs in catalog:
            if cs.can_add_service(biggest):
                new_s = cs.clone()
                new_s.add_service(biggest)
                servers.append(new_s)
                found = True
                break
        if not found:
            print("warning forgot: ", str(biggest))

solution = produire_solution(servers)
print("Solution: \n" + solution)
print("Score: ", calcule_score(scenario, servers))