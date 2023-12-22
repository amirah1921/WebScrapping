import csv

def read_recipes(filename):
    recipes = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipes.append(row)
    return recipes

def suggest_recipe(available_ingredients, recipes):
    for recipe in recipes:
        required_ingredients = recipe['Ingredients'].split(',')
        if all(ingredient in available_ingredients for ingredient in required_ingredients):
            return recipe['Recipe']
    return "No matching recipe found."

def main():
    filename = 'recipes.csv'
    recipes = read_recipes(filename)

    print("Available Ingredients (comma-separated):")
    user_input = input().split(',')

    suggested_recipe = suggest_recipe(user_input, recipes)

    print("\nSuggested Recipe:")
    print(suggested_recipe)

if __name__ == "__main__":
    main()
