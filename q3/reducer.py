#!/usr/local/bin/python3.7

import sys
import pandas as pd

df = pd.read_csv(sys.stdin)
df.columns = ['order_year', 'country', 'item_type', 'units_sold']

output = df.groupby(['order_year','country','item_type'])[['units_sold']].agg([min, max]).reset_index()

for item in [','.join(element.split()) for element in output.to_string(header=False,index=False).split('\n')]:
    print(item)