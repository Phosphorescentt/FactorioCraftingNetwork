import requests
import networkx as nx
import networkx.algorithms.community as nx_comm

import matplotlib.pyplot as plt

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


def create_network_from_items(items):
    # There is a way to do this recursively so that you don't have to iterate
    # over everything twice but I'm too tired/lazy/dumb to figure that out :)
    G = nx.DiGraph()
    G.add_nodes_from(items)

    for item in items:
        recipe = item.recipe
        for ingredient in recipe.ingredients:
            iid = ingredient["id"]
            iamount = ingredient["amount"]

            # Find the node in the graph corresponding to the item with id iid
            n = None
            for node in G.nodes():
                if node.id == iid:
                    n = node
                    break

            if n is None:
                raise Exception("Something went wrong!")

            if iid is not None:
                G.add_edge(n, item, weight=iamount)

    return G

def render_digraph(G, filename):
    plt.figure(figsize=(50, 50))

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_edges(G, pos)

    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, font_size=8)

    plt.savefig(filename)


def render_digraph_communities(G, communities, filename):
    colours = ["red", "blue", "yellow", "green", "aquamarine", "orange", "pink", "plum", "purple", "black", "white"]
    plt.figure(figsize=(50, 50))

    pos = nx.spring_layout(G)

    for i, comm in enumerate(communities):
        nx.draw_networkx_nodes(G, pos, nodelist=comm, node_color=colours[i])

    nx.draw_networkx_edges(G, pos)

    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, font_size=8)

    plt.savefig(filename)

if __name__ == "__main__":
    r = requests.get("https://kevinta893.github.io/factorio-recipes-json/recipes.min.json")
    items = [Item(i) for i in r.json()]
    G = create_network_from_items(items)

    # print("Rendering graph")
    # render_digraph(G, "graph.png")

    print("Rendering communities")
    communities = nx_comm.louvain_communities(G)
    print(len(communities))
    # render_digraph_communities(G, communities, "comm_graph.png")

