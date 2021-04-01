from utils.servers import Server
from utils.scenario import Scenario

def calcule_score(scenario: Scenario, serveurs: Server):
    score = 0

    for server in serveurs:
        score += server.co2production + server.co2usage * scenario.nb_annees

    return score

def produire_solution(serveurs: Server):
    res = ""
    for serv in serveurs:
        res += serv.nom + "," + ",".join([service.nom for service in serv.running_services]) + "\n"
    return res
