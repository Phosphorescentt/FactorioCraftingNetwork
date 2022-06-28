import json

with open("data.raw.json") as f:
    j = json.load(f)

recipes = j["recipe"]

# with open("data.json", "w") as f:
#     json.dump(recipes, f)

r = recipes["advanced-circuit"]
# print(r["ingredients"])
