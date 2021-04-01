import csv
from utils.servers import Server
from utils.scenario import Scenario
from utils.score import *

server_catalog = "codecontest_fr_df_accenturehackathome/servers_catalog.csv"
scenario_file = "ctstfr0280_input_1.csv"

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

servers = []
for service in scenario.services:
    # si on a aucun serveur
    if len(servers) == 0:
        for serv in catalog:
            if serv.can_add_service(service):
                new_server = serv.clone()
                new_server.add_service(service)
                servers.append(new_server)
                break
    else:
        # on a des serveurs
        can_hold_service = False
        # on cherche un serveur qui peut contenir les données
        for serv in servers:
            if serv.can_add_service(service):
                can_hold_service = True
                serv.add_service(service)
                break
        else:
            # on doit créer un nouveau serveur
            for serv in catalog:
                if serv.can_add_service(service):
                    new_server = serv.clone()
                    new_server.add_service(service)
                    servers.append(new_server)
                    break

print("Score: ", calcule_score(scenario, servers))
solution = produire_solution(servers)
print("Solution: \n" + solution)

res_to_file("input_1.csv", solution)