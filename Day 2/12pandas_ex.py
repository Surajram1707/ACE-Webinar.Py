import pandas as pd 

d = {"Name" : ["Ajay","Athitya","Hagrid","Harry"], 
     "Age": [21,20,450,27],
     "City": ["Karaikudi","Chennai","London","Paparapatti"]}

datafr = pd.DataFrame(d)
print(datafr)
print(datafr["City"])
print(datafr.loc[1:3,"Age":"City"])
print(datafr["Age"].max()) #min, mean, median, mode, count, sum, variance and even more
