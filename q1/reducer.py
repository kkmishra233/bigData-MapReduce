import sys
import pandas as pd

df = pd.read_csv(sys.stdin)
df.columns = ['order_year', 'country', 'item_type', 'unit_price']

df["unit_price"] = pd.to_numeric(df["unit_price"], downcast="float")
output = df.groupby(['order_year','country','item_type'])[['unit_price']].mean().reset_index()

for item in [','.join(element.split()) for element in output.to_string(header=False,index=False).split('\n')]:
    print(item)