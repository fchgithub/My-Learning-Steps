'''
Created on Oct 30, 2015

@author: Fatemeh
'''
from __future__ import print_function 
from pyspark import SparkContext, SparkConf
import os
#import math
import numpy as np
     
def distance(p, c):
    return np.sqrt(np.sum((p - c)**2))

def closestCtr(point, _):
    print ('uuuuuuu')
    mini = float("+inf")
    index = -1
    for crt_i in range(len(_)):
        dist = distance(point, _[crt_i])
        if  dist < mini:
            mini = dist
            index = crt_i
    print ('index i %d: ' %index)
    return index  
    
def sum_dist(p1, p2):
    return p1 + p2

def toVector(line):
    return  np.array([float(x) for x in line.split(' ')])

def divide_list(point, count):
    return point / count
     
     
     
     
     
def main(sc, minPartition):
    dataRDD = sc.textFile(os.environ["SPARK_HOME"] + "\data.txt", minPartitions= minPartition)
    points = dataRDD.map(toVector)
    KCtrs = points.takeSample(False, 2, 1)
    KctrsB = sc.broadcast(KCtrs)
    convergeDist = 0.1
    tempDist = 1.0
    while tempDist > convergeDist:
        closest = points.map(lambda point: (closestCtr(point, KctrsB.value), (point, 1)))
        closestStat = closest.reduceByKey(lambda p1_c1, p2_c2: (sum_dist(p1_c1[0], p2_c2[0]), (p1_c1[1] + p2_c2[1])))
        #print(closestStat.collect())
        newCtrs = closestStat.map(lambda cs: (cs[0], divide_list(cs[1][0], cs[1][1])))
        newCenters = newCtrs.collect()
        tempDist = sum(np.sum((KCtrs[iK] - p) ** 2) for (iK, p) in newCenters)
        
        for (iK, p) in newCenters:
            KCtrs[iK] = p
            
        KctrsB = sc.broadcast(KCtrs)
        
        

    print("K-centers: " , KCtrs)


if __name__ == "__main__":
    sparkconf = SparkConf().setAppName("K-MEANS").setMaster("local[*]")
    sc = SparkContext(conf = sparkconf)
    minPartition = 2;
    main(sc, minPartition)
    
    sc.stop()
    

