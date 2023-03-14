spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
  
   return [food["name"] for food in spicy_foods]
  
    
def get_spiciest_foods(spicy_foods):
     return [food for food in spicy_foods if food["heat_level"] > 5]
    
    
def print_spicy_foods(spicy_foods):
    pepper = "🌶"
    spicy_food_list = [(spicy_foods[n]["name"], spicy_foods[n]["cuisine"], spicy_foods[n]["heat_level"]) for n in range(len(spicy_foods))]
    individual_spicy_food = [spicy_food_list[n] for n in range(len(spicy_food_list))]
    for n in range(len(individual_spicy_food)):
        print(f"{individual_spicy_food[n][0]} ({individual_spicy_food[n][1]}) | Heat Level: {pepper * individual_spicy_food[n][2]}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    
    [cuisine_food] = [spicy_foods[n] for n in range(len(spicy_foods)) if spicy_foods[n]["cuisine"] == cuisine]
    return cuisine_food

def print_spiciest_foods(spicy_foods):
     pepper = "🌶"
     spiciest_food_list = [(spicy_foods[n]["name"], spicy_foods[n]["cuisine"], spicy_foods[n]["heat_level"]) for n in range(len(spicy_foods)) if spicy_foods[n]["heat_level"] > 5]
     ind_spiciest_foods = [spiciest_food_list[n] for n in range(len(spiciest_food_list))]
     for n in range(len(ind_spiciest_foods)):
        print(f"{ind_spiciest_foods[n][0]} ({ind_spiciest_foods[n][1]}) | Heat Level: {pepper * ind_spiciest_foods[n][2]}")
    
def get_average_heat_level(spicy_foods):
    spicy_food_heats = [spicy_foods[n]["heat_level"] for n in range(len(spicy_foods))]
    avg_heat = sum([spicy_food_heats[n] for n in range(len(spicy_food_heats))]) / len(spicy_food_heats)
    return avg_heat
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
