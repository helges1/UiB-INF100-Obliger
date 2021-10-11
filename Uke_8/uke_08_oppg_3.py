def meal_list(fridge, ingredient_list):
    count = 0
    for i in fridge:
        if i in ingredient_list:
            count += 1
        
    return count == len(ingredient_list)

def meal_options(fridge, meals):

  meal_options_ls = []

  count = 0
  len_meals = len(meals) 

  while count < len_meals:
      if meal_list(fridge,meals[count][1]) == True:
        meal_options_ls.append(meals[count][0])
      count += 1

  return meal_options_ls

# # contents of my fridge, in a list
# my_fridge = ["tomato sauce", "mustard", "potatoes", "carrots", "chicken", "frozen fish"]

# # ingredients for all 4 meals in tuple
# meals = [
#     # name of dish [0], ingredients [1]
#     ("fish_sticks", ["frozen fish", "potatoes", "mustard"]),
#     ("chicken_curry", ["chicken", "curry paste", "carrots", "potatoes", "rice"]),
#     ("chicken_veg", ["chicken", "potatoes", "carrots"]),
#     ("pasta", ["spaghetti", "tomato sauce"]),
# ]

# print(meal_list(my_fridge, meals[0][1]))

# print(meal_options(my_fridge, meals))