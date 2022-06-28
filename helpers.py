import networkx as nx
import matplotlib.pyplot as plt


class Recipe:
    def __init__(self, ingredients, time, crafting_yield):
        self.ingredients = ingredients
        self.time = time
        self.item_yield = crafting_yield

class Item:
    def __init__(self, j):
        self.id = j["name"]

        try:
            time = j["energy-required"]
        except:
            time = 1

        try:
            crafting_yield = j["result_count"]
        except:
            crafting_yield = 1

        self.recipe = Recipe(j["ingredients"], time, crafting_yield)

        # self.category = j["category"]
        # self.id = j["id"]
        # self.recipe = Recipe(j["recipe"])
        # self.type = j["type"]
        # self.wiki_link = j["wiki_link"]

    def __repr__(self):
        # return f"<Item object with id {self.id}>"
        return self.id


def render_graph(G, pos, filename):
    plt.figure(figsize=(50, 50))

    nx.draw_networkx_nodes(G, pos=pos)
    nx.draw_networkx_edges(G, pos)

    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, font_size=8)

    plt.savefig(filename)

def render_graph_communities(G, pos, communities, filename):
    colours = ["red", "blue", "yellow", "green", "aquamarine", "orange", "pink", "plum", "purple", "black", "white"]
    plt.figure(figsize=(50, 50))

    for i, comm in enumerate(communities):
        nx.draw_networkx_nodes(G, pos, nodelist=comm, node_color=colours[i % len(colours)])

    nx.draw_networkx_edges(G, pos)

    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, font_size=8)

    plt.savefig(filename)

def create_network_from_items(items):
    G = nx.Graph()
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
