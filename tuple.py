# tuple just look same like a list except we use parenthesis instead of square brackets
simple_foods = ('chicken grilled', 'Chicken Avocado', 'roasted beef', 'salad')
for food in simple_foods:
    print(food.title())
# Chicken Grilled
# Chicken Avocado
# Roasted Beef
# Salad

# the restaurant change its menu, let's replace 2 items in simple_foods
simple_foods = ('wing', 'Chicken Avocado', 'roasted beef', 'family pack')
for food in simple_foods:
    print(food.title())
# Wing
# Chicken Avocado
# Roasted Beef
# Family Pack