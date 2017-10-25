
total = 0   # set global calories equal to 0


def fats():             # set up for fat
    global total
    fat = input("Please enter the grams of fat you ate today: ")
    while not fat.isdigit():        # check for errors
        fat = input("There was an error, please enter the fat you ate again with proper numbers: ")
    fat_1 = int(fat)
    fat_1 *= 9          # calculation for grams of fat
    total += fat_1
    print("You ate ", fat_1, "calories from fat today.")


def carbs():            # set up for carbs
    global total
    carb = input("Please enter the the grams of carbs you ate today: ")
    while not carb.isdigit():           # check for errors
        carb = input("There was an error, please enter the carbs you ate again with proper numbers")
    carb_1 = int(carb)
    carb_1 *= 4         # calculation for grams of carbs
    total += carb_1
    print("You ate, ", carb_1, "calories from carbs.")


def proteins():         # set up for proteins
    global total
    protein = input("Please enter the grams of protein you ate today: ")
    while not protein.isdigit():        # check for erros
        protein = input("There was an error, please enter the protein you ate again with proper numbers.")
    protein_1 = int(protein)
    protein_1 *= 4          # calculation for grams of protein
    total += protein_1
    print("You ate, ", protein_1, "calories from protein")

# final numbers
fats()
carbs()
proteins()
print("You ate a total of ", total, "calories today.")
