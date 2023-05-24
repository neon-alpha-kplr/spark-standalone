# spark-standalone

## Install

### Setting working dir
mkdir spark_standalone
cd spark_standalone

### System update
sudo apt update -y
sudo apt upgrade -y

### Install JDK
apt-get install default-jdk -y
java --version

### Install Scala
sudo apt-get install scala -y
scala -version

scala
> println("Test successful");

### Install Spark
wget https://dlcdn.apache.org/spark/spark-3.4.0/spark-3.4.0-bin-hadoop3.tgz
tar -xvzf spark-3.4.0-bin-hadoop3.tgz
sudo mv spark-3.4.0-bin-hadoop3 /mnt/spark

### Update PATH
nano ~/.bashrc
export SPARK_HOME=/mnt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
source ~/.bashrc

### Test run Spark
start-master.sh
Check listening port
ss -tpln | grep 8080
stop-master.sh

### Install PySpark
pip install pyspark

### Run a simple Python script
from pyspark.sql import SparkSession

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