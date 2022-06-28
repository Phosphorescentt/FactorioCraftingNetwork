import json
import networkx as nx
# import networkx.algorithms.community as nx_comm

import helpers
from helpers import Item


if __name__ == "__main__":
    # r = requests.get("https://kevinta893.github.io/factorio-recipes-json/recipes.min.json")
    with open("data/data.json") as f:
        j = json.load(f)

    # items = [Item(j[i]) for i in j]

    items = []
    for i in j:
        print(i)
        items.append(Item(j[i]))

    G = helpers.create_network_from_items(items)

    # pos = nx.spring_layout(G, 30)
    # communities = nx_comm.asyn_fluidc(G, 5)


    # print("Rendering graph")
    # render_graph(G, pos, "graph.png")

    # print("Rendering communities")
    # render_graph_communities(G, pos, communities, "comm_graph.png")

    # print("======================================")

    # for c in communities:
    #     print(c)

    components = nx.connected_components(G)

    for c in components:
        print(c)

