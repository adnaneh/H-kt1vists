from utils.servers import Server
from utils.scenario import Scenario

def calcule_score(scenario: Scenario, serveurs: Server):
    score = 0

    for server in serveurs:
        score += server.co2production + server.co2usage * scenario.nb_annees

    return score