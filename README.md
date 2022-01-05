Run docker trong terminal folder

$ docker-compose up
Coppy file từ local lên namenode container

Up file test.txt để test

$ docker cp <src-path> <container>:<dest-path> 
Push data lên hdfs

$ hdfs dfs -mkdir -p /user/data
$ hadoop fs -copyFromLocal /path/in/linux /hdfs/path
Tạo file code đọc data từ hdfs qua elasticsearch

Chạy lệnh để tăng config cho elasticsearch chạy

wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
Spark

Gắn path cho spark-submit

alias spark-submit='/spark/bin/spark-submit'
Code mẫu để test hệ thống

import sys
from pyspark import SparkConf
from pyspark.context import SparkContext

# thay địa chỉ master thành địa chỉ của mình
sc = SparkContext.getOrCreate(SparkConf().setAppName("BigData").setMaster("spark://3b256839d254:7077"))
# Địa chỉ của file trên hdfs
text_file = sc.textFile("hdfs://namenode:9000//user/hadoop/data/test.txt")
counts = text_file.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a,b: a+b)
output = counts.collect()
counts.saveAsTextFile("hdfs://namenode:9000//user/hadoop/data/output.txt")
sc.stop()
Cần làm: Tạo file python để đọc file lưu sang elasticsearch
