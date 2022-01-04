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