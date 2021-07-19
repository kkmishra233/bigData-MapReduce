import sys
import pandas as pd

def read_mapper_output(file, separator):
    for line in file:
        yield line.rstrip().split(separator)

data = read_mapper_output(sys.stdin, separator=',')
df = pd.DataFrame(data, columns=['order_date', 'country', 'item_type', 'units_sold'])
output = df.groupby(['order_date', 'country', 'item_type'])['units_sold'].sum()

for key,value in output.to_dict().items():
    print((",").join(key)+","+value)