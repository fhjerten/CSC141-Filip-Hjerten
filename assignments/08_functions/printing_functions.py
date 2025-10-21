def print_models(unprinted_designs, completed_models):

# I simulate printing each design, until none are left
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):

# I show all the models that were printed
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(model)
