#Lab_10-5

def add_foods(foods):
    sixth_letter=[]
    non_foods=[]
    short_foods=[]
    #three types of possible answers so that the inputs are sorted
    for food in foods:
        try:
            sixth_letter.append(food[5])
        except TypeError:
            non_foods.append(food)

        

