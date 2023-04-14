import pandas as pd

a = [1, 2, 3, 4, "string", 5.65]

a = pd.Series(a, index=['a', 'b', 'c', 'd', 'e', 'f'])

# passing key value pair to Series
calories = {"day1": 420, "day2": 380, "day3": 390}

calories = pd.Series(calories)

# data frame is a 2D data structure, like a 2D array, or a table with rows and columns.
# series is a 1D data structure, like a list, or an array with a single column.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

data = pd.DataFrame(data)

print(data)