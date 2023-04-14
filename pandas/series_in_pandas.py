import pandas as pd

a = [1, 2, 3, 4, "string", 5.65]

a = pd.Series(a, index=['a', 'b', 'c', 'd', 'e', 'f'])

# passing key value pair to Series
calories = {"day1": 420, "day2": 380, "day3": 390}

calories = pd.Series(calories)

print(calories)