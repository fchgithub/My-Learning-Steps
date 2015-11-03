'''
Created on Oct 28, 2015

@author: Fatemeh
'''
from __future__ import print_function
from pyspark import SparkContext, SparkConf
import os

def main(sc, partitions):
    dataRDD = sc.textFile(os.environ["SPARK_HOME"]+"/data.txt", partitions)
       
    sortedRDD = dataRDD.flatMap(lambda x: x.split(' ')).map(lambda x: (int(x), 1))\
        .sortByKey(lambda x: x)
        
    output = sortedRDD.collect()
    for (num, _) in output: 
        print(num, end=' ')
    
if __name__ == "__main__":
    '''
        Usage: sort a file with multiple columns
    '''
    # Configure the Spark environment
    sparkConf = SparkConf().setAppName("sortApp").setMaster("local[2]")
    sc = SparkContext(conf = sparkConf)

    main(sc, 2)
    sc.stop()
    