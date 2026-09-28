from recipe import recipes


def save_recipes():
    file = open("recipes.txt", "w")

    for name in recipes:
        recipe = recipes[name]

        file.write(name + "~")
        file.write(recipe["time"] + "~")
        file.write(",".join(recipe["ingredients"]) + "~")
        file.write(",".join(recipe["steps"]) + "~")
        file.write(",".join(recipe["tips"]) + "\n")

    file.close()


def load_recipes():
    file = open("recipes.txt", "r")

    for line in file:
        data = line.strip().split("~")

        if len(data) == 5:
            name = data[0]
            time = data[1]
            ingredients = data[2].split(",")
            steps = data[3].split(",")
            tips = data[4].split(",")

            recipes[name] = {
                "time": time,
                "ingredients": ingredients,
                "steps": steps,
                "tips": tips
            }

    file.close()
