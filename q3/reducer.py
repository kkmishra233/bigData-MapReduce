#!/usr/local/bin/python3.7
import sys

# partition
partition_Collection = {}
for line in sys.stdin:
    line = line.strip()
    order_year, country, item_type, units_sold = line.split(",")
    if (order_year,country,item_type) in partition_Collection.keys():
        partition_Collection[(order_year,country,item_type)].append(int(units_sold))
    else:
        partition_Collection[(order_year,country,item_type)] = []
        partition_Collection[(order_year,country,item_type)].append(int(units_sold))

# reducer
for (order_year,country,item_type) in partition_Collection.keys():
    max_unit_sold=max(partition_Collection[(order_year,country,item_type)])
    min_unit_sold=max(partition_Collection[(order_year,country,item_type)])
    print(f'{order_year},{country},{item_type},{max_unit_sold},{min_unit_sold}')
