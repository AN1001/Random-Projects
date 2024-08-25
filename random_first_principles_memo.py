#uses memory addresses to get random (not optimal)
root_seed = 10

def get_random_seed():
    global root_seed
    root_seed = id(root_seed + 1)
    return root_seed

def random_range(lower_bound, upper_bound):
    seed = get_random_seed()
    diff = upper_bound - lower_bound
    return lower_bound + (seed % diff)
    
print(random_range(10,50))
print(random_range(10,50))
print(random_range(10,50))
