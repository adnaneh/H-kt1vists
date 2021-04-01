

import numpy as np
import numba 
import pandas as pd 

@numba.jit(nopython=True)
def pick_smallest_server(service_array, services_catalog_params):
    inc = 0
    for server_type in services_catalog_params:
        diff = (server_type - service_array >= 0).all()
        if diff:
            return(inc)
        inc+= 1 

@numba.jit(nopython=True)
def pick_valid_servers_server(service_array, services_catalog_params):
    res = []
    inc = 0
    for server_type in services_catalog_params:
        diff = (server_type - service_array >= 0).all()
        if diff:
            res.append(inc)
        inc+= 1 
    return(res)

@numba.jit(nopython=True)
def pick_remaining_server(service_array, servers_remains):
    inc = 0
    for server_type in servers_remains:
        diff = (server_type - service_array >= 0).all()
        if diff:
            return(inc)
        inc+= 1 
    return(-1)


file_name = 'C:/Users/adnane/Downloads/ctstfr0280_input_5.csv'

with open(file_name) as f:
    data = f.readlines() 

n_services = len(data)-1

services_params = np.zeros((n_services, 4)) #storage, ram, cores, server_id
servers_types = -np.ones(n_services) # server_type, remaining_storage, ram, cores
server_remains = np.zeros((n_services, 3)) # server_type, remaining_storage, ram, cores


# Servers types from 1 to 20
file_name = 'C:/Users/adnane/Desktop/servers_catalog.csv'
services_catalog = pd.read_csv(file_name)
param_columns = ['disk', 'ram', 'cores']
# services_catalog = services_catalog.drop(columns = ['model'])

# services_catalog = services_catalog.to_numpy() #prod_cost, yearly_cost, storage, ram, cores

# initialisation
initial_line = True
inc = 0
for service_line in data:
    if initial_line:
        n_years = int(service_line)
        initial_line = False
        
        # calculate server cost
        services_catalog['costs'] = services_catalog['co2production'] + services_catalog['co2usage'] * n_years
        services_catalog = services_catalog.sort_values('costs')
        
        sorted_models = services_catalog['model']
        services_catalog_params = services_catalog[param_columns].to_numpy()
        # sort servers by cost
        
        continue
    
    service_line_split = service_line.split(',')[1:]
    service_line_split = [int(x) for x in service_line_split]
    
    server = pick_remaining_server(np.array(service_line_split), server_remains)
    if server == -1: 
        server = pick_smallest_server(np.array(service_line_split), services_catalog_params)
        servers_types[inc] = server
        server_remains[inc] = services_catalog_params[server]
        service_line_split.append(inc)

    else:  
        server_remains[server] -= np.array(service_line_split)
        service_line_split.append(server)

    service_line_split = np.array(service_line_split)
    
    services_params[inc] = service_line_split 
    
    
    
    if inc%10000 == 0:
        print(inc)
    inc+=1


# print(servers_types)   
inc = 0
server_services_map = {}
server_names_map = {}
for service in services_params:
    server_id  = int(service[-1])
    server = servers_types[server_id]
    server_name = sorted_models[server]
    
    if server_id in server_names_map:
        server_services_map[server_id].append(inc)
    else:
        server_names_map[server_id] = server_name
        server_services_map[server_id] = [inc]

    inc += 1

result = []
for server_id in server_services_map:
    res = [server_names_map[server_id]]
    for service in server_services_map[server_id]:
        res.append('service_' + str(service))
    result.append(res)
# print(result)

pd.DataFrame(result).to_csv('exemple.csv', index = False, header = False)

if False:
    # Tests
    pick_smallest_server(service_line_split[:-1], services_catalog_params)
    pick_valid_servers_server(service_line_split[:-1], services_catalog_params)

    services_catalog['model'].iloc[pick_valid_servers_server(service_line_split[:-1], services_catalog_params)]
