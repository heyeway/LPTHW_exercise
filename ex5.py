my_name = 'Zed A. Shaw'
my_age = 35
#my_height = 74
my_height_cms = 74 * 2.54
#my_weight = 180
my_weight_kgs = 180 * 0.45359237
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
#print(f"He's {my_height} inches tall.")
print(f"He's {my_height_cms} centimeters tall.")
#print(f"He's {my_weight} pounds heavy.")
print(f"He's {my_weight_kgs} kilograms heavy.")
print("Actually that's too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height_cms + my_weight_kgs
print(f"If I add {my_age}, {my_height_cms}, and {my_weight_kgs} I get {total}.")
