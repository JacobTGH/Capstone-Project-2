
class Recipe(): # Creating the recipe class
    
    def __init__(self, recipe_name, recipe_ingredients, recipe_instructions, recipe_cooking_time, recipe_dietary_info): # Constructor for new recipes        
        self.title = recipe_name.title()
        self.ingredients = recipe_ingredients
        self.instructions = recipe_instructions
        self.cooking_time = recipe_cooking_time
        self.dietary_info = recipe_dietary_info.capitalize()

    def set_title(self, recipe_name): # Function for setting the name of the recipe and forcing user input to title case
        self.title = recipe_name.title()
    
    def get_title(self): # Function for retrieving the name of the recipe
        return self.title
    
    def set_ingredients(self, recipe_ingredients): # Function for setting the list of ingredients
        self.ingredients = recipe_ingredients

    def get_ingredients(self): # Function for retrieving the ingredient list
        return self.ingredients
    
    def set_instructions(self, recipe_instructions): # Function for setting the instructions
        self.instructions = recipe_instructions

    def get_instructions(self): # Function for retrieving the instructions
        return self.instructions
    
    def set_cooking_time(self, recipe_cooking_time): # Function for setting the cooking time
        self.cooking_time = recipe_cooking_time

    def get_cooking_time(self): # Function for retrieving the cooking time
        return self.cooking_time
    
    def set_dietary_info(self, recipe_dietary_info): # Function for setting the dietary info
        self.dietary_info = recipe_dietary_info.capitalize()

    def get_dietary_info(self): # Function for retrieving the dietary info
        return self.dietary_info

    def get_details(self): # Function for displaying all of the information in the recipe
        print(f"Recipe: {self.title} \n"
              f"Dietary information: {self.dietary_info} \n"
              f"This recipe takes {self.cooking_time} minutes to cook")
        print("The ingredients are: " + ', '.join(self.ingredients).capitalize())        
        length = len(self.instructions)
        for i in range(length):
            i = int(i)
            print(f"{i + 1}. {self.instructions[i].capitalize()}")
            
recipes = {} #Dictionary to store the recipes

class recipe_management(): #Class for management of receipes
    def add_recipe():
        recipe_name = input("Enter recipe name: ")
        recipe_ingredients = input("Enter ingredients (separated by commas): ").split(",")
        recipe_instructions = input("Enter instructions: ")
        recipe_cooking_time = input("Enter cooking time: ")
        recipe_dietary = input("Enter dietary info: ")

        recipe = {
            "Name" : recipe_name,
            "Ingredients" : recipe_ingredients,
            "Instructions" : recipe_instructions,
            "Cooking time" : recipe_cooking_time,
            "Dietary" : recipe_dietary
        }
        recipes[recipe_name] = recipe
        print ("Recipe add with success!")

def update_recipe():
 #options to choose what want to update and then show the existing information to update (?)

 def view_recipe(recipe_name):
    if recipe_name in recipes:
        recipe = recipes[recipe_name]
        print(f"Recipe: {recipe_name}")
        print(f"Ingredients: {recipe['Ingredients']}")
        print(f"Instructions: {recipe['Instructions']}")
        print(f"Cooking time: {recipe['Cooking time']}")
        print(f"Dietary: {recipe['Dietary']}")

    def delete_recipe():
        if recipe_name in recipes:
            del recipes[recipe_name]
            print("Recipe deleted!")
        else:
            print("Recipe could not be found. Try again.")

    def menu():
        while True:
            print("--- Recipe system Management ---")
            print("1. Add recipe")
            print("2. Update recipe details")
            print("3. View recipe")
            print("4. Delete recipe")
            print("5. Exit")

            option = input("Enter your option (1-4): ")

            if option == "1":
                add_recipe()
            elif option == "2":
                recipe_name = input("Enter recipe name:")
                update_recipe(recipe_name)
            elif option == "3":
                recipe_name = input("Enter recipe name: ")
                view_recipe(recipe_name)
            elif option == "4":
                recipe_name = input("Enter recipe name: ")
                delete_recipe(recipe_name)
            elif option == "5":
                break
            else:
                print("Invalid option. Choose option 1, 2, 3, 4 or 5.")
