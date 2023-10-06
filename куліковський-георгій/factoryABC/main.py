from creator_one import Creator_One
from creator_two import Creator_Two


product_one = Creator_One().create_product()
print(product_one.class_method())


product_two = Creator_Two().create_product()
print(product_two.class_method())