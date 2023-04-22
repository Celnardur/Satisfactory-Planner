import json

def get_item_amt_dict(ingredients, input_raw):
    item_amt = {}
    for item in ingredients:
        item_amt[input_raw["items"][item["item"]]["name"]] = item["amount"]
    
    return item_amt


def main():
    with open('input_data.json', 'r') as fp:
        input_raw = json.load(fp)

    recipies = {}
    for class_name,info in input_raw["recipes"].items():
        if info["inMachine"] == False:
            continue # for now we only care about automation planning
        recipe = {}
        recipe["time"] = info["time"]
        recipe["input"] = get_item_amt_dict(info["ingredients"], input_raw)
        recipe["output"] = get_item_amt_dict(info["products"], input_raw)

        recipies[info["name"]] = recipe

    with open('game_data.json', 'w') as fp:
        json.dump(recipies, fp, indent=4)

if __name__ == "__main__":
    main()
