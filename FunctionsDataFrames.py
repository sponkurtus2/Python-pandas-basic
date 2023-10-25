import numpy as np
import pandas as pd

tennis_set = {
    'First set points': [15, 15, 30],
    'Second set points': [30, 60, 30],
    'Third set points': [30, 60, 60]
    }

tennis_set_dataFrame = pd.DataFrame(data=tennis_set)

# Max function -> Used to find the highest value in an array

# We can do the max function with this, it's not as usefully as the example
# below, but i think its interesting
'''
    First_set_points = [15, 15, 30]
    First_set_max = max(*First_set_points)
'''

First_set_max = max(tennis_set['Third set points'])
print(First_set_max)

# We can also use a for to get all the highest values
Max_per_set = {}
for set_name, points in tennis_set.items():
    Max_per_set[set_name] = max(points)

print(Max_per_set)


# Min functions -> The same as max function, but with the min value
First_set_min = min(tennis_set['First set points'])
print(First_set_min)

# Mean function -> returns the average value
Calorie_burnage = [240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

Average_calorie_burnage = np.mean(Calorie_burnage)
print(Average_calorie_burnage)