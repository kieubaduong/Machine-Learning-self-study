from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

data = pd.read_csv('dataset/missing_data.csv', header=None, delimiter=';')

# strategy can be mean, median, most_frequent
# mean replace missing values with the mean of the column
# median replace missing values with the median of the column
# most_frequent replace missing values with the most frequent value of the column
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# imputer.fit returns the imputer object with the mean values of the columns
imputer = imputer.fit(data.values)

# imputer.transform returns the data with the missing values replaced
result = imputer.transform(data.values)

print(result)