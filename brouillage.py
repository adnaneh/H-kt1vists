import csv
from utils.servers import Server
from utils.service import Service
from utils.scenario import Scenario
from utils.score import *
from tqdm import tqdm

input_number = "6"

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

#print(sum(scenario.services, start=Service(["", 0, 0, 0])))
# sorting services
scenario.services = sorted(scenario.services, reverse=True)

servers_full = []
servers = []
while len(scenario.services) > 0:
    min_service = min(scenario.services)

    # filter servers that cant add services
    to_remove = []
    for s in servers:
        if not s.can_add_service(min_service):
            to_remove.append(s)
    for e in to_remove:
        servers_full.append(e)
        servers.remove(e)
    servers = sorted(servers, reverse=False) # du plus petit au plus grand espace

    # on remplit les serveurs existants
    for server in servers:
        to_remove = []
        for service in scenario.services:
            if server.can_add_service(service):
                server.add_service(service)
                to_remove.append(service)
        for element in to_remove:
            scenario.services.remove(element)

    if len(scenario.services) == 0:
        break

    # on crée un nouveau serveur
    # on prend le plus gros element
    sum_service = sum(scenario.services, start=Service(["", 0, 0, 0]))
    max_service = max(scenario.services)
    scenario.services.remove(max_service)
    if catalog[-1].can_add_service(sum_service):
        for cs in catalog:
            if cs.can_add_service(sum_service):
                ns = cs.clone()
                servers.append(ns)
                break
        else:
            print("warning cannot find server big enough at creation")
    else:
        for cs in catalog[::-1]:
            if cs.can_add_service(max_service):
                ns = cs.clone()
                ns.add_service(max_service)
                servers.append(ns)
                break
        else:
            print("warning cannot find server big enough at creation")

## --------------------------
solution = produire_solution(servers + servers_full)
print("Solution: \n" + solution)
print("Score: ", calcule_score(scenario, servers + servers_full))