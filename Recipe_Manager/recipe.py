import tkinter as tk
from PIL import ImageTk, Image #load image and place in frame - logo widget

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
        return f"Recipe: {self.title} \n" \
            f"Dietary information: {self.dietary_info} \n" \
            f"This recipe takes {self.cooking_time} minutes to cook\n" \
            f"The ingredients are: {', '.join(self.ingredients).capitalize()}\n" \
            f"Instructions:\n" + "\n".join(f"{i+1}. {ins.captalize()}" for i, ins in enumerate(self.instructions))        

# Recipe Manager
class RecipeManager:
    def __init__(self):
        self.recipes = [] #save recipes

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.get_title().lower() == recipe_name.lower():
                self.recipes.remove(recipe)
                return True
        return False

    def search_recipe(self, keyword):
        found_recipes = []
        for recipe in self.recipes:
            if keyword.lower() in recipe.get_title().lower():
                found_recipes.append(recipe)
        return found_recipes

#initiallize
window = tk.Tk()
window.title("Recipe Management System")
window.eval("tk::PlaceWindow . center") #window will open on centre of the screeen
bg_colour = "black"

#FRAME WIDGET: groups widgets 
frame1 = tk.Frame(window, width = 500, height = 600, bg = bg_colour) #change the colour later
frame1.grid(row=0, column=0)
frame1.pack_propagate(False) #background colour to all page

#frame1 widgets
# logo_img = ImageTk.PhotoImage(Image.open('logo.png').convert('RGB'))
# logo_widget = tk.Label(frame1, image = logo_img) # converting to widget, tkinter doesn't have an specific
# logo_widget.image = logo_img
# logo_widget.pack() #place widget in frame

tk.Label(frame1,
         text = "Recipe Management System",
         bg = bg_colour,
         fg = "white",
         font = ("TkMenuFont", 14)
         ).pack()

# Initialize recipe manager
recipe_manager = RecipeManager()

# GUI Functions
def add_recipe():
    title = recipe_title.get()
    ingredients = recipe_ingredients.get().split(',')
    instructions = recipe_instructions.get("1.0", tk.END).split('\n')
    cooking_time = recipe_cooking_time.get()
    dietary_info = recipe_dietary_info.get()

    recipe = Recipe(title, ingredients, instructions, cooking_time, dietary_info)
    recipe_manager.add_recipe(recipe)

    recipe_title.delete(0, tk.END)
    recipe_ingredients.delete(0, tk.END)
    recipe_instructions.delete("1.0", tk.END)
    recipe_cooking_time.delete(0, tk.END)
    recipe_dietary_info.delete(0, tk.END)

    update_recipe_listbox()

def search_recipe():
    keyword = search_keyword.get()
    found_recipes = recipe_manager.search_recipe(keyword)

    search_results.delete("1.0", tk.END)
    if found_recipes:
        for recipe in found_recipes:
            search_results.insert(tk.END, recipe.get_details() + "\n\n")
    else:
        search_results.insert(tk.END, "No recipes found with the given keyword!")

def update_recipe():
    selected_recipe = recipe_listbox.get(tk.ACTIVE)
    if selected_recipe:
        new_title = recipe_title.get()
        new_ingredients = recipe_ingredients.get().split(',')
        new_instructions = recipe_instructions.get("1.0", tk.END).split('\n')
        new_cooking_time = recipe_cooking_time.get()
        new_dietary_info = recipe_dietary_info.get()

        for recipe in recipe_manager.recipes:
            if recipe.get_title() == selected_recipe:
                recipe.set_title(new_title)
                recipe.set_ingredients(new_ingredients)
                recipe.set_instructions(new_instructions)
                recipe.set_cooking_time(new_cooking_time)
                recipe.set_dietary_info(new_dietary_info)

        recipe_title.delete(0, tk.END)
        recipe_ingredients.delete(0, tk.END)
        recipe_instructions.delete("1.0", tk.END)
        recipe_cooking_time.delete(0, tk.END)
        recipe_dietary_info.delete(0, tk.END)

        update_recipe_listbox()


# GUI Elements for adding and searching and updating recipes
update_button = tk.Button(frame1, text="Update Recipe", command=update_recipe)
update_button.pack()

recipe_title = tk.Entry(frame1)
recipe_title.pack()

recipe_ingredients = tk.Entry(frame1)
recipe_ingredients.pack()

recipe_instructions = tk.Text(frame1, width=40, height=10)
recipe_instructions.pack()

recipe_cooking_time = tk.Entry(frame1)
recipe_cooking_time.pack()

recipe_dietary_info = tk.Entry(frame1)
recipe_dietary_info.pack()

add_button = tk.Button(frame1, text="Add Recipe", command=add_recipe)
add_button.pack()

search_keyword = tk.Entry(frame1)
search_keyword.pack()

search_button = tk.Button(frame1, text="Search Recipe", command=search_recipe)
search_button.pack()

search_results = tk.Text(frame1, width=40, height=10)
search_results.pack()

recipe_listbox = tk.Listbox(frame1, width=40, height=10)
recipe_listbox.pack()

def update_recipe_listbox():
    recipe_listbox.delete(0, tk.END)
    for recipe in recipe_manager.recipes:
        recipe_listbox.insert(tk.END, recipe.get_title())

update_recipe_listbox()

#run
window.mainloop() #displays app until the user closes it
