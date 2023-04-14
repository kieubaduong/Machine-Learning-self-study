import pandas as pd

myDataset = {
    'cars' : ["BMW", "Volvo", "Ford"],
    'passings'  : [3, 7, 2],
}

myVariable = pd.DataFrame(myDataset)

print(myVariable)