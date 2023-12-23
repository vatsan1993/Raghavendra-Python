# pantry item and quantity Recipe ingredient needed and instructions.
# create consume buyIngredients methods.(python inheritance ex6)

class Item:
    def __init__(self, name, quantity = 0):
        self._name = name
        self._quantity = quantity

    def get_item_name(self):
        return self._name

    def get_item_quantity(self):
        return self._quantity

    def is_sufficient(self, quantity):
        if quantity <= self._quantity:
            return True
        else:
            return False

    def consume_item(self, quantity):
        if self.is_sufficient(quantity):
            self._quantity -= quantity
            return True
        return False

    def fill_up(self, quantity):
        self._quantity += quantity

    def item_match(self, ingredient_name):
        return self._name == ingredient_name

    def __str__(self):
        return f"Item Name: {self._name}, Quantity: {self._quantity}"

class Recipe:
    def __init__(self, name):
        self._name = name
        self._ingredients = {}
        self._instructions = []

    def get_name(self):
        return self._name

    def get_ingredients(self):
        return self._ingredients.copy()

    def get_instructions(self):
        return self._instructions.copy()

    def add_ingredient(self, name, quantity):
        self._ingredients[name] = quantity

    def add_instruction(self, instruction):
        self._instructions.append(instruction)

    def __str__(self):
        output = f'Dish:{self._name}\nIngredients'
        for  ingredient, quantity in self._ingredients.items():
            output += f'\n\t'+ "{:20} {:5d}".format(ingredient, quantity)
        output += "\nInstructions:"
        for index,instruction in enumerate(self._instructions):
            output += f'\n\tStep{index+1} {instruction} '
        output+="\n"
        return output


class Pantry:
    def __init__(self, recipes= [], ingredients= []):
        self._recipes = recipes
        self._ingredients = ingredients

    def get_recipes(self):
        return  self._recipes

    def get_ingredients(self):
        return self._ingredients

    def search(self, name):
        for recipe in self._recipes:
            if recipe.get_name().lower() == name.lower():
                return recipe
        return None

    def add_recipe(self, name):
        recipe = self.search(name)
        if recipe == None:
            recipe = Recipe(name)
            self._recipes.append(recipe)
            return recipe , True # representing a new recipe has been created
        return recipe, False # recipe already exists

    def get_ingredient(self, name, quantity):
        # used to check the available quantity is sufficient to make a dish
        for ingredient in self._ingredients:
            if ingredient.get_item_name() == name:
                status= ingredient.is_sufficient(quantity)
                return {name: ingredient.get_item_quantity()} , status
        return {name: 0} , False

    def search_ingredient(self, name):
        # used to get and ingredient to fill it up.
        for ingredient in self._ingredients:
            if ingredient.get_item_name() == name:
                return ingredient
        return None

    def make_dish(self, name):
        recipe = self.search(name)
        if recipe == None:
            return 'Recipe does not exist'
        else:
            items_needed = recipe.get_ingredients()
            items_not_available = {}
            # items_needed will be a dictionary
            status = True
            for item, quantity in items_needed.items():
                data, sufficient = self.get_ingredient(item, quantity)

                if sufficient:
                  return True
                else:
                    # adds existing values first
                    # then adds new value
                    # ** will spread a keyword argument(unpacks)
                    items_not_available = {**items_needed, **data}
                    # dict1 = {'a': 10}
                    # dict2 = {'b': 20}
                    # dict3 = {**dict1, **dict2}
                    # print(dict3)
                    status = False
            # if all ingredients exists we reduce the quantity that we need to make the dish
            if status == True:
                for name, quantity in items_needed.items():
                    ingredient = self.search_ingredient(name)
                    ingredient.consme(quantity)
                return 'Recipe has been made'

            return items_not_available

    def add_ingredient(self, name, quantity):
        self._ingredients.append(Item(name, quantity))

    def fillItem(self, name, quantity):
        ingredient = self.search_ingredient(name)
        if ingredient == None:
            self.add_ingredient(name, quantity)
        else:
            ingredient.fill_up(quantity)



pantry = Pantry()
def load_data():
    with open('ingredients.txt', 'r') as ingredients_file:
         for line in ingredients_file:
            line = line.strip("\n")
            name, quantity = line.split(", ")
            pantry.add_ingredient(name, quantity)
    with open('recipes.txt', 'r') as recipes_file:
        data = recipes_file.readlines()
        for i in range(0, len(data), 3):
            name, ingredients, instructions = data[i: i+3]
            recipe, exists = pantry.add_recipe(name.strip("\n"))
            instructions = instructions.split(', ')
            ingredients = ingredients.split(', ')
            for ingredient_str in ingredients:
                ingredient, quantity = ingredient_str.strip("\n").split(":")
                recipe.add_ingredient(ingredient, int(quantity))

            for step in instructions:
                recipe.add_instruction(step.strip("\n"))

def display_main_menu():
    print(f'''Welcome to Pantry Management System
Menu
1. Get All Recipes
2. Get All Ingredients
3. Make Dish
4. Fill Ingredient
5. Create new Recipe
6. quit''')
def get_all_recipies():
    for recipe in pantry.get_recipes():
        print(recipe)
def get_ingredients():
    for ingredient in pantry.get_ingredients():
        print(ingredient)

def make_dish():
    name = input('Enter the name of the dish you want to make: ')
    status = pantry.make_dish(name)
    if type(status) == str:
        print(status)
    else:
        for item, quantity in status.items():
            print(item, quantity)
        print("These items are not enough to make the dish")
def fill_item():
    name = input('Enter the name of the ingredient you want to restock: ')
    quantity = int(input('Enter the quantity: '))
    pantry.fillItem(name, quantity)

def create_recipe():
    name = input("Enter name of the dish")
    recipe, new_recipe = pantry.add_recipe(name)
    if new_recipe:
        while True:
            ingredient = input("Enter the ingredient or type 'end' to end the ingredients: ")
            if ingredient == 'end':
                break
            quantity = int(input('Enter the quantity needed: '))
            recipe.add_ingredient(ingredient, quantity)

        step_num = 1
        while True:
            step = input(f"Enter step{step_num} or 'end' to end the instructions: ")
            if step == 'end':
                break
            recipe.add_instruction(step)
            step_num += 1
    else:
        print('Recipe already exists.')

def write_ingredients():
    # ingredients in the pantry. not the ingredients for a recipe.s
    ingredients = pantry.get_ingredients()
    with open('ingredients.txt', 'w') as ingredients_file:
        for ingredient  in ingredients:
            ingredients_file.write(f'{ingredient.get_item_name()}, {ingredient.get_item_quantity()}\n')

def write_recipes():
    recipes = pantry.get_recipes()
    with open('recipes.txt','w') as recipes_file:
        for recipe in recipes:
            recipes_file.write((f'{recipe.get_name().strip(" ")}\n'))
            ingredients = recipe.get_ingredients() # a dictionary not a list of Item class objects
            ingredients_str = ''

            for ingredient, quantity in ingredients.items():
                ingredients_str += f'{ingredient.strip(" ")} : {quantity}, '
            # this will add extra , at the end. we need to remove it before we write it to the file.
            ingredients_str = ingredients_str.strip(', ')
            recipes_file.write(ingredients_str + '\n')

            instructions = recipe.get_instructions()
            instructions_str = ''
            for instruction in instructions:
                instructions_str += f'{instruction}, '
            # this will add extra , at the end. we need to remove it before we write it to the file.
            instructions_str = instructions_str.strip(', ')
            recipes_file.write(instructions_str+ '\n')


def main():
    load_data()
    while True:
        display_main_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            get_all_recipies()
        elif choice == 2:
            get_ingredients()
        elif choice == 3:
            make_dish()
        elif choice == 4:
            fill_item()
        elif choice == 5:
            create_recipe()
        elif choice == 6:
            print("Bye")
            write_ingredients()
            write_recipes()
            break

main()




