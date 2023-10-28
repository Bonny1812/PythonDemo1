import examplepackage
import pyspark
from pyspark.sql import SparkSession
import os 
from pyspark.conf import SparkConf
from pyspark import SparkContext
spark = SparkSession.builder.master('local').getOrCreate()
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession


examplepackage.example_module.example_function(spark)