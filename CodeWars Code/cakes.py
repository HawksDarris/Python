def cakes(recipe, available):
    # Check if there are enough ingredients for the recipe
    for ingredient, amount in recipe.items():
        if ingredient not in available or available[ingredient] < amount:
            return 0

    # Calculate how many cakes can be made
    maxyield = float('inf')
    for ingredient, amount in recipe.items():
        maxyield = min(maxyield, available[ingredient] // amount)

    return maxyield

recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe,available))
