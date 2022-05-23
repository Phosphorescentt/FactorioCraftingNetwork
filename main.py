import requests
import networkx


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
        return self.id


def add_items_to_network_via_recipe(G, items):
    G = networkx.Graph()
    return G

def create_network_from_items(items):
    for item in items:

        pass
    pass


if __name__ == "__main__":
    r = requests.get("https://kevinta893.github.io/factorio-recipes-json/recipes.min.json")
    items = [Item(i) for i in r.json()]
    G = create_network_from_items(items)
