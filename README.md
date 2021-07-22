questions:—
========

columns : index,region,country,item_type,sales_channel,order_priority,
order_date,order_id,ship_date,units_sold,unit_price,unit_cost,
total_revenue,total_cost,total_profit

q1 - Average unit_price by country for a given item type in a certain year

q2 - Total units_sold by year for a given country and a given item type

q3 - Find the max and min units_sold in any order for each year by country
for a given item type. Use a custom partitioner class instead of default hash based.

q4 - What are the top 10 order id for a given year by the total_profit


Execute mapper and reducer in local:
========
cat ../geosales.csv | python3.7 mapper.py | python3.7 reducer.py > output.txt


steps to execute map reduce task 
========

install docker in the system

install git in the system

git clone git@github.com:big-data-europe/docker-hadoop.git

cd docker-hadoop

docker-compose up -d 

docker ps 

now enter into containers

install python on all runninng containers of hadoop

docker exec -it namenode bash

docker exec -it resourcemanager bash

docker exec -it nodemanager bash

docker exec -it historyserver bash

docker exec -it datanode bash

steps:
apt-get update

apt-get -y install wget gcc make build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev curl libbz2-dev

cd /tmp/

wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz

tar xzf Python-3.7.6.tgz

cd Python-3.7.6

./configure --enable-optimizations

make altinstall

rm -rf /tmp/Python-3.7.6.tgz /tmp/Python-3.7.6

python3.7 -m pip install pandas

exit()


docker exec -it namenode /bin/bash

cd /

mkdir map_reduce

chmod -R 777 map_reduce

exit()

docker cp <complete_foldeer_content> namenode:/map_reduce/

docker exec -it namenode /bin/bash

hadoop fs -mkdir -p /input

hdfs dfs -put ./input/geosales.csv /input/

command :
========
hadoop jar /map_reduce/hadoop-streaming-3.2.1.jar \
-input /input/geosales.csv \
-output /input/output/q1/ \
-file /map_reduce/q1/mapper.py -mapper 'python3.7 mapper.py' \
-file /map_reduce/q1/reducer.py -reducer 'python3.7 reducer.py'

hadoop jar /map_reduce/hadoop-streaming-3.2.1.jar \
-input /input/geosales.csv \
-output /input/output/q2/ \
-file /map_reduce/q2/mapper.py -mapper 'python3.7 mapper.py' \
-file /map_reduce/q2/reducer.py -reducer 'python3.7 reducer.py'

hadoop jar /map_reduce/hadoop-streaming-3.2.1.jar \
-input /input/geosales.csv \
-output /input/output/q3/ \
-file /map_reduce/q3/mapper.py -mapper 'python3.7 mapper.py' \
-file /map_reduce/q3/reducer.py -reducer 'python3.7 reducer.py'

hadoop jar /map_reduce/hadoop-streaming-3.2.1.jar \
-input /input/geosales.csv \
-output /input/output/q4/ \
-file /map_reduce/q4/mapper.py -mapper 'python3.7 mapper.py' \
-file /map_reduce/q4/reducer.py -reducer 'python3.7 reducer.py'

command with custom partitionar:
========
hadoop jar /map_reduce/hadoop-streaming-3.2.1.jar \
-D map.output.key.field.separator=, \
-D num.key.fields.for.partition=2 \
-D mapreduce.job.reduces=2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-input /input/geosales.csv \
-output /input/output/q4/ \
-file /map_reduce/q4/mapper.py -mapper 'python3.7 mapper.py' \
-file /map_reduce/q4/reducer.py -reducer 'python3.7 reducer.py'


*Note:*
========
num.key.fields.for.partition=2 this is no of fields configurable like if data is 
male,krishna,28,10k
female,alice,28,10k
then if i want to creae partition on based of male only then i will pass num.key.fields.for.partition=1 

map.output.key.field.separator: Key separator in map
num.key.fields.for.partition: Specify how many columns (columns separated by separators)
as the basis of partition, the same will be divided into the same reduce, 
if there is no separator or the number of separators is less than the specified bibliography, 
the key is regarded as the entire row, value Is empty

-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner  
Used in conjunction with the above two configuration items, otherwise it has no effect


see the output:
==============

hdfs dfs -ls /input/output/

hdfs dfs -cat /input/output/q1/part-00000

hdfs dfs -cat /input/output/q2/part-00000

hdfs dfs -cat /input/output/q3/part-00000

hdfs dfs -cat /input/output/q4/part-00000

get complete output directory in localsystem

downlaod the output in local system:
====================================
hdfs dfs -get /input/output /map_reduce/

