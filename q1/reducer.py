import sys
import pandas as pd
import numpy as np
def read_mapper_output(file, separator):
    for line in file:
        yield line.rstrip().split(separator)

data = read_mapper_output(sys.stdin, separator=',')
df = pd.DataFrame(data, columns=['order_date', 'country', 'item_type', 'unit_price'])
df["unit_price"] = pd.to_numeric(df["unit_price"], downcast="float")
output = df.groupby(['order_date', 'country', 'item_type']).agg({"unit_price": [np.size, np.mean]})

for key,value in output.to_dict().items():
    for value_key,value_value in value.items():
        print((",").join(value_key)+","+str(value_value))