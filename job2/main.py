
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col


def demo_df():

    # Extract
    df = spark.read.format("csv").option("header", "true").load(planes_file)
    # Transform
    df = df.withColumn("NewCol", lit(0)).filter(col("model").isNotNull())
    # Load
    df.write.format("delta").mode("overwrite").saveAsTable("{}.planes".format(database))
    # Verify
    resDf = spark.sql("SELECT * FROM planes")
    resDf.show()


if __name__ == '__main__':

    app_name = sys.argv[1]
    app_config_file = sys.argv[2]

    print(app_name)
    print(app_config_file)

    spark = SparkSession.builder.appName(app_name).getOrCreate()

    # extract config

    c_json = spark.read.option("multiline", "true").json(app_config_file)
    database = c_json.select("database").first()[0]
    planes_file = c_json.select("planes_file").first()[0]

    demo_df()
