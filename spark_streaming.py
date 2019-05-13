import socket
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

ssc = StreamingContext(sc, 10)

ssc.checkpoint("/sandbox/sandbox8/tmp/errorfiles")

lines = ssc.socketTextStream("130.6.50.208", 5555)

counts = lines.flatMap(lambda line: line.split(" ")).filter(lambda word:"OutOfMemoryError" in word).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b)
counts.pprint()
ssc.start()
ssc.awaitTermination


nc -l 5555
