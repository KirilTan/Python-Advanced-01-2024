def cookbook(*recipes):
    """
    Organizes and sorts recipes by cuisine, then formats and returns a string listing the recipes.

    This function assists in arranging recipes systematically based on cuisine. It sorts the recipes
    by the number of recipes in each cuisine in descending order. In cases where two or more cuisines
    have the same number of recipes, they are sorted in ascending alphabetical order by cuisine name.
    Within each cuisine group, the recipes are sorted alphabetically by the recipe's name.

    Each recipe within a cuisine group is displayed along with the necessary ingredients.

    Parameters:
    - recipes (tuple): A variable number of arguments, each a tuple containing three elements:
        1. The recipe's name (str).
        2. The cuisine (str).
        3. A list of ingredients (list of str).

    Returns:
    - str: A formatted string listing the sorted recipes by cuisine, along with the count of recipes
           in each cuisine group and the ingredients for each recipe.

    Note:
    - Each input tuple is unique and represents a distinct recipe and its associated cuisine.
    - The list of ingredients for each recipe is never empty.

    Example:
    print(cookbook(
        ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
        ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
        ...
    ))

    Output:
    Italian cuisine contains 3 recipes:
      * Margherita Pizza -> Ingredients: pizza dough, tomato sauce, mozzarella
      * Spaghetti Bolognese -> Ingredients: spaghetti, tomato sauce, ground beef
      ...
    """
    # Organize recipes by cuisine
    cuisine_dict = {}
    for name, cuisine, ingredients in recipes:
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = []
        cuisine_dict[cuisine].append((name, ingredients))

    # Sort cuisines by the number of recipes and alphabetically
    sorted_cuisines = sorted(cuisine_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    # Format the output string
    output = []
    for cuisine, recipes in sorted_cuisines:
        output.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        sorted_recipes = sorted(recipes, key=lambda x: x[0])
        for name, ingredients in sorted_recipes:
            ingredients_str = ", ".join(ingredients)
            output.append(f"  * {name} -> Ingredients: {ingredients_str}")

    return "\n".join(output)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

print('\n', '------------------------------------------------------------------------------------------', '\n')

print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))

print('\n', '------------------------------------------------------------------------------------------', '\n')

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
