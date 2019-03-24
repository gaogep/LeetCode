states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut'])
stations = {
    'kone': set(['id', 'nv', 'ut']),
    'ktwo': set(['wa', 'id', 'mt']),
    'kthr': set(['or', 'nv', 'ca']),
    'kfou': set(['nv', 'ut']),
    'kfiv': set(['ca', 'az'])
}

final_station = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_station.add(best_station)

print(final_station)