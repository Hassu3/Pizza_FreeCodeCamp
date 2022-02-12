

class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        veg_str = ""
        if self.vegetarian:
            veg_str = " - VEGETARIAN"
        print(f"PIZZA {self.name} : {self.price}$" + veg_str)
        print(", ".join(self.ingredients))
        print()


class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    last_number = 0

    def __init__(self):
        CustomPizza.last_number += 1
        self.number = CustomPizza.last_number
        super().__init__("Custom " + str(self.number), 0, [])
        self.ask_user_for_ingredients()
        self.compute_price()

    def ask_user_for_ingredients(self,):
        print()
        print(f"Ingredients for pizza numer {self.number}")
        while True:
            ingredient = input("Add an ingredient (or press ENTER to finish)")
            if ingredient == "":
                return
            self.ingredients.append(ingredient)
            print(f'Yoy have {len(self.ingredients)} ingredient(s) : {", ".join(self.ingredients)}')

    def compute_price(self):
        self.price = self.BASE_PRICE + self.PRICE_PER_INGREDIENT * len(self.ingredients)


pizzas = [
    Pizza("4 cheeses", 8.99, ("blue cheeses", "brie", "emmental", "mozarella"), True),
    Pizza("Hawai", 9.5, ("tomato", "pineaplle", "onion")),
    Pizza("4 seasons", 11, ("eggs", "tomato", "emmental", "ham")),
    Pizza("Vegetarian", 7.8, ("mushrooms", "tomato", "oignons", "bell pepper"), True),
    CustomPizza(),
    CustomPizza()
]

for i in pizzas:
        i.display()
