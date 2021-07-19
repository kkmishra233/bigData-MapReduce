import sys
import pandas as pd

def read_mapper_output(file, separator):
    for line in file:
        yield line.rstrip().split(separator)

data = read_mapper_output(sys.stdin, separator=',')
df = pd.DataFrame(data, columns=['order_date', 'order_id', 'total_profit'])
output = df.sort_values(by=["total_profit"],ascending=False).groupby('order_date').head(10)
result = output.sort_values(by='order_date')
for item in [','.join(element.split()) for element in result.to_string(header=False,index=False).split('\n')]:
    print(item)