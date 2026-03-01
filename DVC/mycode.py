import pandas as pd
import numpy as np
import os

data = {
    'name':['Anuraj','Bob','Rohit'],
    'Age':[12,34,5],
    'City':['New york','Los angles','Chicago']
}

df = pd.DataFrame(data)

# adding a new role in the data
new_row_loc = {'name':'Gf1','Age':23,'City':'Agartala'}

df.loc[len(df.index)] =  new_row_loc

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path, index=False)

print(f'CSV file saved to {file_path}')