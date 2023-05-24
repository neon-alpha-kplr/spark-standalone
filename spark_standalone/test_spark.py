from pyspark.sql import SparkSession

# Create Spark session with local[4] as Gitpod instance has 4 cores
spark = (SparkSession
    .builder
    .appName("Spark test")
    .master("local[4]")
    .getOrCreate()
)

print('Session started')

df1=spark.createDataFrame([["one","two","three"],[1,2,3]])
df1.write.mode('overwrite').csv("test.csv")
print("CSV file saved")

df2=spark.read.csv("test.csv")
df2.show()