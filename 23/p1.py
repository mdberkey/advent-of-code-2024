def get_tripples(graph):
    tripples = []
    for k, v in graph.items():
        for n in v:
            for n2 in graph[n]:
                if k in graph[n2]:
                    trip_set = set([k, n, n2])
                    if trip_set not in tripples:
                        tripples.append(trip_set)
    return tripples

if __name__ == "__main__":
    lines = open("23/i1").read().splitlines()
    graph = {}
    for line in lines:
        l, r = line.split("-")
        if l not in graph:
            graph[l] = set()
        graph[l].add(r)
        if r not in graph:
            graph[r] = set()
        graph[r].add(l)

    tripples = get_tripples(graph)
    t_trips = []
    for trip in tripples:
        for val in trip:
            if val.startswith("t"):
                t_trips.append(trip)
                break

    print(len(t_trips))