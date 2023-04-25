#to have a list of names with gwa for students file

import random

#create a function to generate random gwa
def gwa_generator():
    #generate a gwa between 1.0 and 5.0
    random_gwa = random.uniform(1.0, 5.0)
    #return the gwa to 2 decimal places
    return round(random_gwa, 2)

print(gwa_generator())