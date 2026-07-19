import pandas as pd
data = {
    "Name":["Harshad","Amit","Priya"],
    "Age":[21,22,34]
}
df = pd.DataFrame(data)
print(df.iloc[0])