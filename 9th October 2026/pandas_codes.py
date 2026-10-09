# dataframe -> a simple representation of data gives more methods to operate on daata
# de -> extract->transform->load->etl process

import pandas as pd
df=pd.read_csv("orders.csv")
# print(df)
#print(df.head())#first few rows like 1st 5
#print(df.tail())#last few rows
#print(df.columns)#know col names alone
#print(df.shape) #no of rows and cols
#print(df.dtypes) #datatypes of cols
#df.info() #more information about data
#select by condition
# print(df["product"])
# print(df[["order_id","product","amount"]])
#filter
# delivered=df.query("status == 'Delivered'")
# print(delivered)
#
# result=df.query("amount>20000")
# print(result)
#
# print(df["status"].value_counts()) #does operations of groupby
# result=(df.groupby("status").size()) #groupby
# print(result)
#string to date and added month as new column
df["order_date"]=pd.to_datetime(df["order_date"])
df["month"]=df["order_date"].dt.month
print(df)