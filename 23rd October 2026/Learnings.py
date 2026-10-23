from google.colab import files
 
uploaded = files.upload()
#upload same retail_transactions_100k dataset
!pip install pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
.appName("Working with dataframes") \
.getOrCreate()
df = spark.read.csv(
"retail_transactions_100k.csv",
header=True,
inferSchema=True
)
df.show()


#drop and filter gives copy original never modified
df2=df.drop("rating")
df2.show(5)
#drop multiple columns
df2=df.drop(
    "rating",
    "payment_method",
    "customer_name"
)
df2.show(5)

print(df2.columns)

from pyspark.sql.functions import col
df2=df.filter(
    col("status")!="Cancelled"
)
df2.show()

df2=df.dropDuplicates()

df2=df.drop_duplicates(
    ["customer_id"]
)
df2.show()

df2=df.drop_duplicates(
    ["customer_id","product_id"]
)

df2=df.distinct()

df.select("city").distinct().show()
#drop null value rows
df2=df.na.drop()
#drop rows with null values in given column
df2=df.na.drop(
    subset=["payment_method"]
)

df.orderBy("unit_price").show()
df.sort("unit_price").show()

from pyspark.sql.functions import col
df.orderBy(col("unit_price").desc()).show()

df.orderBy(
    col("category").asc(),
    col("unit_price").desc()
).show()

df2=df.withColumn(
    "gross_amount",
    col("unit_price")*col("quantity")
)

df2.orderBy(
    col("gross_amount").desc()
).show()

# Tasks
# Sort unit price ascending.

# Sort unit price descending.

# Sort quantity descending
# .
# Sort by category and then unit price descending.

# Create gross_amount and show top 10 orders.

# Sort by region and then city.

# Sort by status and then quantity descending.

# Display the 5 lowest-priced transactions.

df2.orderBy(col("unit_price").asc()).show()
df2.orderBy(col("unit_price").desc()).show()
df2.orderBy(col("quantity").desc()).show()
df2.orderBy(col("Category").asc(),col("unit_price").desc()).show()
df2.withColumn("gross_amount",col("unit_price")*col("quantity")).orderBy(col("gross_amount").desc()).show(10)
df2.orderBy(col("region").asc(),col("city").asc()).show()
df2.orderBy(col("status").asc(),col("quantity").desc()).show()
df2.orderBy(col("unit_price").asc()).limit(5).show()

from pyspark.sql.functions import sum, avg, min, max, count, col
df.select(
    sum("quantity").alias("total_quantity")
).show()
df.select(
    avg("unit_price").alias("average_price")
).show()
df.select(
    max("unit_price").alias("highest_price")
).show()
df.select(
    count("*").alias("total_records"),
    sum("quantity").alias("total_quantity"),
    avg("unit_price").alias("average_price"),
    min("unit_price").alias("lowest_price"),
    max("unit_price").alias("highest_price")
).show()

# Create gross_amount.
# Find total gross sales.
# Create discount_amount.
# Find total discount given.
# Create final_amount.
# Find total final sales.
# Find total sales from Delivered orders only.
# Find the average value of Delivered orders.
# Count Electronics transactions.
# Count Cancelled transactions.
df2=df2.withColumn("gross_amount",col("unit_price")*col("quantity"))
df2.select(sum("gross_amount").alias("total_gross_sales")).show()
df2=df2.withColumn("discount_amount",col("unit_price")*col("quantity")*0.1)
df2.select(sum("discount_amount").alias("total_discount_given")).show()
df2=df2.withColumn("final_amount",col("gross_amount")-col("discount_amount"))
df2.select(sum("final_amount").alias("total_final_sales")).show()
df2=df2.filter(col("status")=="Delivered")
df2.select(sum("gross_amount").alias("total_delivered_sales")).show()
df2.select(avg("gross_amount").alias("average_delivered_sales")).show()
df2=df2.filter(col("category")=="Electronics")
df2.select(count("*").alias("total_electronics_transactions")).show()
df2=df2.filter(col("status")=="Cancelled")
df2.select(count("*").alias("total_cancelled_transactions")).show()

#groupby
df.groupBy("category").count().show()
df.groupBy("status").count().show()
df.groupBy("category").agg(
    sum("quantity").alias("total_quantity")
).show()
df.groupBy("category").agg(
    count("*").alias("total_orders"),
    sum("quantity").alias("total_quantity"),
    avg("unit_price").alias("average_price"),
    min("unit_price").alias("lowest_price"),
    max("unit_price").alias("highest_price")
).show()

#joins
customers_data = [
    ("C00001", "Aman Retail", "Hyderabad", "Corporate"),
    ("C00002", "Blue Mart", "Mumbai", "Retail"),
    ("C00003", "Fresh Basket", "Bangalore", "Retail"),
    ("C00004", "Prime Stores", "Delhi", "SMB"),
    ("C00005", "Quick Shop", "Pune", "Corporate")
]
 
customers_columns = [
    "customer_id",
    "customer_name_master",
    "customer_city",
    "segment"
]
 
customers_df = spark.createDataFrame(
    customers_data,
    customers_columns
)
 
customers_df.show()

joined_df=df.join(
    customers_df,
    on="customer_id",
    how="inner"
)
joined_df.show()

joined_df=df.join(
    customers_df,
    on="customer_id",
    how="left"
)
joined_df.show()

joined_df=df.join(
    customers_df,
    on="customer_id",
    how="right"
)
joined_df.show()

joined_df=df.join(
    customers_df,
    on="customer_id",
    how="outer"
)
joined_df.show()


#Ranking
 from pyspark.sql.window import Window
from pyspark.sql.functions import (
    col,
    row_number,
    rank,
    dense_rank,
    sum,
    avg,
    lag,
    lead
) 

window_spec = Window.partitionBy("category") \
    .orderBy(col("avg_price").desc())
ranked_products = product_df.withColumn(
    "rank",
    row_number().over(window_spec)
)
ranked_products.show()
#for this avg_price colis not present in our df so use unit_price
window_spec = Window.partitionBy("category") \
    .orderBy(col("unit_price").desc())
ranked_products = df.withColumn(
    "rank",
    row_number().over(window_spec)
)
ranked_products.show()

ranked_products.filter(col("rank")<=3).show()

#date
from pyspark.sql.functions import col, to_date
 
df2 = df.withColumn(
    "order_date",
    to_date(col("order_date"), "yyyy-MM-dd")
)

from pyspark.sql.functions import year
df2.withColumn(
    "year",
    year("order_date")).select("order_date","year")\
.show()
from pyspark.sql.functions import month
df2.withColumn(
    "month",
    month("order_date")).select("order_date","month")\
.show()
from pyspark.sql.functions import dayofmonth
df2.withColumn(
    "day",
    dayofmonth("order_date")).select("order_date","day")\
.show()



