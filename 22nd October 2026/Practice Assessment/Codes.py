from google.colab import files
uploaded = files.upload()

!pip install pyspark

from pyspark.sql import SparkSession
spark=SparkSession.builder \
        .appName("Pyspark Exercise") \
        .getOrCreate()

df = spark.read.csv(
"retail_transactions_100k.csv",
header=True,
inferSchema=True
)

df.show()

df.printSchema()

df.count()

#Exercise Set 1 — Basic DataFrame Operations
df.show(20)
df.printSchema()
print(df.columns)
print(df.count())
df.select("order_id","product_name","city","quantity","unit_price").show()
df.filter(df.category=="Electronics").show()
df.filter(df.city=="Hyderabad").show()
df.filter(df.quantity>3).show()
df.filter(df.unit_price>20000).show()
df.filter(df.status=="Delivered").show()

#Exercise Set 2 — Multiple Conditions
df.filter((df.category=="Electronics") & (df.city=="Hyderabad")).show()
df.filter((df.status=="Delivered") & (df.region=="South")).show()
df.filter((df.quantity>2) & (df.unit_price>10000)).show()
df.filter((df.city=="Mumbai") | (df.city=="Pune")).show()
df.filter(df.status!="Cancelled").show()
df.filter((df.category=="Furniture")&(df.unit_price>8000)).show()
df.filter((df.category=="Accessories")&(df.quantity>3)).show()

#Exercise Set 3 — Selecting and Renaming
df.select("order_id","customer_name","product_name","unit_price").show()
df.withColumnRenamed("unit_price","price").show()
df.withColumnRenamed("customer_name","customer").show()
df.drop("rating").show()
new_df=df.drop("customer_name","rating","payment_method")
new_df.show()

#Exercise Set 4 — withColumn()
df2 = df.withColumn(
    "gross_amount",
    col("quantity") * col("unit_price")
)
df2=df2.withColumn(
    "discount_amount",
    col("gross_amount")*col("discount_pct")/100
)
df2=df2.withColumn(
    "final_amount",
    col("gross_amount")-col("discount_amount")
)
from pyspark.sql.functions import lit
df2=df2.withColumn(
    "country",
    lit("India")
)
from pyspark.sql import functions as F
df2=df2.withColumn(
    "high_value",
    F.when(col("final_amount")>=50000,"Yes").otherwise("No")
)
df2.show(10)

#Exercise Set 5 — Conditional Columns
df2=df2.withColumn(
    "order_size",
    F.when(col("final_amount")>=50000,"High")
    .when(col("final_amount")>=15000,"Medium")
    .otherwise("Low")
)
df2=df2.withColumn(
    "quantity_type",
    F.when(col("quantity")>=4,"Bulk")
    .otherwise("Regular")
)
df2=df2.withColumn(
    "delivery_status",
    F.when(col("status")=="Delivered","Completed")
    .when(col("status").isin("Cancelled","Returned"),"Failed")
    .otherwise("In Progress")
)

df2.select(
    "order_size",
    "quantity_type",
    "status",
    "delivery_status"
).show(20)

#Exercise Set 6 — Sorting
df2.orderBy(col("unit_price").desc()).show()
df2.orderBy(col("quantity").desc()).show()
df2.orderBy(col("city").asc()).show()
df2.orderBy(col("region").asc(),
            col("final_amount").desc()).show()
df2.orderBy(col("final_amount").desc()).show(10)

#Exercise Set 7 — Distinct Values
df.select("city").distinct().show()
df.select("region").distinct().show()
df.select("category").distinct().show()
df.select("payment_method").distinct().show()
df.select("customer_id").distinct().count()
df.select("product_id").distinct().count()

#Exercise Set 8 — Aggregations
df2.select(F.sum("quantity").alias("total_quantity")).show()
df2.select(F.sum("gross_amount").alias("total_gross_sales")).show()
df2.select(F.avg("unit_price").alias("average_price")).show()
df2.select(F.max("unit_price").alias("maximum_price")).show()
df2.select(F.min("unit_price").alias("minimum_price")).show()
df2.select(F.sum("discount_amount").alias("total_discount")).show()
df2.select(F.sum("final_amount").alias("final_sales_value")).show()

#Exercise Set 9 — groupBy()
df2.groupby("status").count().show()
df2.groupby("category").count().show()
df2.groupby("city").count().show()
df2.groupby("region").agg(
    F.sum("final_amount").alias("total_sales")).show()
df2.groupby("category").agg(
    F.sum("final_amount").alias("total_sales_by_category")).show()
df2.groupby("category").agg(
    F.avg("unit_price").alias("avg_price_by_category")).show()
df2.groupby("product_name").agg(
    F.sum("quantity").alias("total_quantity_by_product")).show()
df2.groupby("payment_method").agg(
    F.sum("final_amount").alias("total_sales_by_payment_method")).show()
df2.groupby("product_name").agg(
    F.avg("rating").alias("avg_rating_by_product")).show()
df2.groupby("city","status").agg(
    F.count("*").alias("total_orders_by_city_status")).show()

#Exercise Set 10 — Group and Sort
df2.groupby("city").agg(
    F.sum("final_amount").alias("total_sales")).sort(
    col("total_sales").desc()).show()
df2.groupby("product_name").agg(
    F.sum("quantity").alias("total_quantity")).sort(
    col("total_quantity").desc()).show()
df2.groupby("category").agg(
    F.avg("unit_price").alias("avg_price")).sort(
    col("avg_price").desc()).show()
df2.groupby("city").agg(
    F.sum("final_amount").alias("total_sales")).sort(
    col("total_sales").desc()).show(5)
df2.groupby("product_name").agg(
    F.sum("quantity").alias("total_quantity")).sort(
    col("total_quantity").desc()).show(5)
df2.groupBy("customer_id").agg(
    F.sum("final_amount").alias("total_purchase_value")).sort(
    col("total_purchase_value").desc()).show(10)

#Exercise Set 11 — Dates
df2=df2.withColumn(
    "order_date",
    F.to_date(col("order_date"),"yyyy-MM-dd")
)
df2=df2.withColumn(
    "year",
    F.year(col("order_date"))
)
df2=df2.withColumn(
    "month",
    F.month(col("order_date"))
)
df2=df2.withColumn(
    "day",
    F.dayofmonth(col("order_date"))
)
df2.select(
    "order_date", "year", "month", "day"
).show(10)

df2.groupBy("year", "month").count().orderBy(
    "year", "month"
).show()

df2.groupBy("year", "month").agg(
    F.sum("final_amount").alias("total_sales")
).orderBy(
    "year", "month"
).show()

df2.groupBy("year", "month", "category").agg(
    F.sum("final_amount").alias("total_sales")
).orderBy(
    "year", "month", "category"
).show()

df2.groupBy("year", "month", "status").agg(
    F.count("*").alias("total_orders")
).orderBy(
    "year", "month", "status"
).show()

df2.groupBy("year", "month").agg(
    F.sum("final_amount").alias("total_sales")
).orderBy(
    F.col("total_sales").desc()
).show(1)

#Exercise Set 12 — Missing Values
df.filter(
    F.col("payment_method").isNull()
).show()

print(
    df.filter(
        F.col("payment_method").isNull()
    ).count()
)

df.filter(
    F.col("rating").isNull()
).show()

print(
    df.filter(
        F.col("rating").isNull()
    ).count()
)

df_payment = df.fillna({
    "payment_method": "Unknown"
})

df_payment.show()

df_rating = df.fillna({
    "rating": 0
})

df_rating.show()

df_clean = df.dropna(
    subset=["payment_method"]
)

df_clean.show()




















