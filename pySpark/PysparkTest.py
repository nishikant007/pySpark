from pyspark.sql import *

if __name__ == '__main__':
    spark = (
        SparkSession.builder.appName("SparkApp").master("local[4]").getOrCreate()
    )
    numbers = [[1], [2], [3], [4], [5]]
    numberDF = spark.createDataFrame(
        numbers, "Id: int"
    )
    numberDF.show()
