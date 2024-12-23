import networkx as nx

if __name__ == "__main__":
    lines = open("23/i1").read().splitlines()
    edges = []

    for line in lines:
        l, r = line.split("-")
        edges.append((l, r))

    # feels like I'm cheating with nx lol
    graph = nx.Graph()
    graph.add_edges_from(edges)

    all_cliques = list(nx.find_cliques(graph))

    largest_clique = max(all_cliques, key=len)

    largest_clique.sort()

    password = ",".join(largest_clique)

    print(password)
