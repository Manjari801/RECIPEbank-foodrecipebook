 recipe import add_recipe, search_recipe, view_recipes, delete_recipe
from storage import load_recipes, save_recipes


load_recipes()

menu = (
    "1. Add Recipe",
    "2. Search Recipe",
    "3. View All Recipes",
    "4. Delete Recipe",
    "5. Exit"
)


while True:

    print("\n========== MY RECIPE BOOK ==========")

    for option in menu:
        print(option)

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter recipe name: ")
        time = input("Enter cooking time: ")

        ingredient_text = input("Enter ingredients separated by commas: ")
        ingredients = ingredient_text.split(",")

        step_text = input("Enter steps separated by commas: ")
        steps = step_text.split(",")

        tip_text = input("Enter important things to take care of: ")
        tips = tip_text.split(",")

        add_recipe(name, time, ingredients, steps, tips)
        save_recipes()

        print("Recipe added successfully!")


    elif choice == "2":

        name = input("Enter recipe name: ")

        recipe = search_recipe(name)

        if recipe:
            print("\nRecipe:", name)
            print("Cooking Time:", recipe["time"])

            print("\nIngredients:")
            for item in recipe["ingredients"]:
                print("-", item)

            print("\nSteps:")
            for step in recipe["steps"]:
                print("-", step)

            print("\nImportant Things:")
            for tip in recipe["tips"]:
                print("-", tip)

        else:
            print("Recipe not found.")


    elif choice == "3":

        data = view_recipes()

        if len(data) == 0:
            print("No recipes available.")

        else:
            print("\nAvailable Recipes:")

            for name in data:
                print("-", name)


    elif choice == "4":

        name = input("Enter recipe name to delete: ")

        if delete_recipe(name):
            save_recipes()
            print("Recipe deleted successfully.")
        else:
            print("Recipe not found.")


    elif choice == "5":

        print("Thank you for using My Recipe Book!")
        break


    else:
        print("Invalid choice. Please try again.")
