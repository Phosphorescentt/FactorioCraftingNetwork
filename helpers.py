import networkx as nx
import matplotlib.pyplot as plt


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
