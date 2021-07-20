
import sys
for line in sys.stdin:
    # Setting defaults column names
    column_index_dict = {'index':0,'region':1,'country':2,'item_type':3,'sales_channel':4,'order_priority':5,
    'order_date':6,'order_id':7,'ship_date':8,'units_sold':9,'unit_price':10,'unit_cost':11,
    'total_revenue':12,'total_cost':13,'total_profit':14}

    line = line.strip()
    if line.startswith('index'):
        continue
    else:
        splits = line.split(",")
        order_year = splits[column_index_dict['order_date']].split('-')[0]
        country = splits[column_index_dict['country']]
        item_type = splits[column_index_dict['item_type']]
        unit_price = splits[column_index_dict['unit_price']]
        print(f'{order_year},{country},{item_type},{unit_price}')