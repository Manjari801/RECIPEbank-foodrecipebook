recipes = {}


def add_recipe(name, time, ingredients, steps, tips):
    recipes[name] = {
        "time": time,
        "ingredients": ingredients,
        "steps": steps,
        "tips": tips
    }


def search_recipe(name):
    if name in recipes:
        return recipes[name]
    else:
        return None


def view_recipes():
    return recipes


def delete_recipe(name):
    if name in recipes:
        del recipes[name]
        return True
    else:
        return False
