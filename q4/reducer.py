#!/usr/local/bin/python3.7

import sys
import pandas as pd

df = pd.read_csv(sys.stdin)
df.columns = ['order_year', 'order_id', 'total_profit']

output = df.set_index(['order_id']).groupby('order_year')['total_profit'].nlargest(10).reset_index()

for item in [','.join(element.split()) for element in output.to_string(header=False,index=False).split('\n')]:
    print(item)