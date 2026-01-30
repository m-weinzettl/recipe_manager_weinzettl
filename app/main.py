import all_recipes.class_recipe
from app.all_recipes.recipes_list import *
from app.all_recipes.class_recipe import *
from menu.menu_structure import menu_loop


all_recipes.class_recipe.Recipe.show_ingredients(pasta)
all_recipes.class_recipe.Recipe.show_instructions(pasta)
all_recipes.class_recipe.Recipe.show_ingredients(pizza)
all_recipes.class_recipe.Recipe.show_instructions(pizza)
all_recipes.class_recipe.Recipe.show_ingredients(salad)
all_recipes.class_recipe.Recipe.show_instructions(salad)


menu_loop()

