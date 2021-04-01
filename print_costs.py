import csv
from utils.servers import Server
from utils.scenario import Scenario
from utils.score import *
from tqdm import tqdm

NB_ANNEES = 6


server_catalog = "codecontest_fr_df_accenturehackathome/servers_catalog.csv"

catalog = []

# Loading server catalog
with open(server_catalog, "r") as server_file:
    reader = csv.reader(server_file, delimiter=',')
    for idx, row in enumerate(reader):
        if idx != 0:
            catalog.append(Server(row))

# sort server by lowest impact for current scenario
catalog = sorted(catalog, key=lambda server: server.impact_co2(NB_ANNEES))

print([server.model for server in catalog])