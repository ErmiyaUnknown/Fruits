# Shape = Sphere
# Mass = 300g --- 600g
# Volume = 100cm3 --- 500cm3

# Volume == Mass

min_ = 100
max_ = 600


tuple_fruits = (
    
    {"name" : "apple", "shape" : "sphere", "mass" : 350, "volume" : 120},
    {"name" : "mango", "shape" : "square", "mass" : 150, "volume" : 120},
    {"name" : "lemon", "shape" : "sphere", "mass" : 300, "volume" : 100},
    {"name" : "apple2", "shape" : "sphere", "mass" : 500, "volume" : 250},
    
)

bad_fruits = []
good_fruits = []


def print_results(list_fruits):  
    
    print(f"\nnumber of good fruits to eat: 👌👌 {len(set(list_fruits))} 👌👌\ntotal_fruits: 👌👌 {str(list_fruits)} 👌👌\n")
    
    
def fruits(tuple_dictionarys):
    
    good_fruits.clear()
    
    for i in tuple_fruits:
        
        if i.get("shape") == "sphere" and i.get("mass") <= max_ and i.get("mass") >= min_ and i.get("volume") <= max_ and i.get("volume") >= min_:
            
            i.setdefault("category", "good")
            good_fruits.append(i["name"])
            continue
        
    print_results(good_fruits)
    
    
fruits(tuple_fruits)               