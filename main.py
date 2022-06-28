import json
import networkx as nx
import networkx.algorithms.community as nx_comm
import matplotlib.pyplot as plt

import helpers

from random import shuffle


class Recipe:
    def __init__(self, j):
        self.time = j["time"]
        self.item_yield = j["yield"]
        self.ingredients = j["ingredients"]
        pass

class Item:
    def __init__(self, j):
        self.category = j["category"]
        self.id = j["id"]
        self.recipe = Recipe(j["recipe"])
        self.type = j["type"]
        self.wiki_link = j["wiki_link"]

    def __repr__(self):
        # return f"<Item object with id {self.id}>"
        return self.id


if __name__ == "__main__":
    # r = requests.get("https://kevinta893.github.io/factorio-recipes-json/recipes.min.json")
    with open("data.json") as f:
        j = json.load(f)
    items = [Item(i) for i in j]
    G = helpers.create_network_from_items(items)

    pos = nx.spring_layout(G, 30)
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

