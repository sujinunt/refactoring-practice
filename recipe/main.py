from recipe import Recipe

def create_recipe(recipe_name, coffee=0, chocolate=0, sugar=0, milk=0, price=0.0):
    recipe = Recipe(recipe_name)
    recipe.coffee = coffee
    recipe.chocolate = chocolate
    recipe.sugar = sugar
    recipe.milk = milk
    recipe.price = price
    return recipe

if __name__ == '__main__':
    recipe1 = create_recipe("Coffee with sugar", 4, 0, 2, 0, 30.0)
    print(recipe1)

    recipe2 = create_recipe("Latte", 3, 0, 2, 1, 40.0)
    print(recipe2)

    recipe3 = create_recipe("Hot Chocolate", 0, 3, 2, 4, 30.0)
    print(recipe3)
