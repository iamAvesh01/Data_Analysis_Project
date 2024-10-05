import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
file= r"C:\Users\admin\OneDrive\Desktop\All_Data\Amazon Sale Report.csv"
amz = pd.read_csv(file)
amz.dropna(how= "all")
be_missing_value= amz.isnull().sum().sum()
be_missing_value
mis_data_rport = {"toatal missing data": be_missing_value}
dup_value= amz.duplicated().sum()
amz.drop_duplicates().inplace = True
amz.duplicated().sum()
amz.head()
amz["Date"]=pd.to_datetime(amz[
    "Date"],errors= "coerce")
amz.describe()
#total  sales value by size
tottal_v_of_s = amz["Size"].value_counts(
    ascending= False).reset_index()
tottal_v_of_s[tottal_v_of_s["Size"]=="S"]

#status of shipment 
status_of_shipment = amz.groupby("Size")[
    "Courier Status"].value_counts().reset_index()
status_of_shipment
#staus of S size 
status_of_shipment[status_of_shipment["Size"]== "S"]
#total amount by status and size
total_amount_of_status = amz.groupby([
    "Size","Courier Status"])["Amount"].sum().reset_index()
total_amount_of_status
#total amount of S size shipment
Status_of_s_amount= total_amount_of_status[total_amount_of_status["Size"]=="S"]
Status_of_s_amount
#total value of shipment city of s sizeship-city
s_size= amz[amz["Size"]=="S"]
total_value_of_shipment_city = s_size.groupby("Size")[
    "ship-city"].value_counts().reset_index()
total_value_of_shipment_city.head(10)
#value of amount each city 
each_shipment_cost = s_size.groupby([
    "Size","ship-city"])["Amount"].sum().reset_index()
each_shipment_cost["Number_of_shipment"]= total_value_of_shipment_city["count"]
each_shipment_cost= each_shipment_cost[["Size","ship-city","Number_of_shipment","Amount"]]
each_shipment_cost.head(10)
#total value and amount of each states
States_vise_valume = s_size.groupby(["Size","ship-state"])[
    "Amount"].sum().reset_index()
A= amz["ship-state"].value_counts().reset_index()
States_vise_valume["Total count"]= A["count"]
States_vise_valume=States_vise_valume[["Size","ship-state","Total count","Amount"]]
States_vise_valume.head(10)
# total  sales by country
Total_sales= amz["ship-country"].value_counts().reset_index()
Total_sales
#total sales buisness to buisness
Total_b2b= amz["B2B"].value_counts().reset_index()
Total_b2b
# date vise fullfillment 
dates_fullfilment= amz.groupby(["Date","Category"])[
    "Fulfilment"].value_counts().reset_index()
dates_fullfilment
#catagory vise status and value count
Status_cat= amz.groupby(["Fulfilment","Status"])[
    "Category"].value_counts().reset_index()
#cancled by seller
seller_ship_value= Status_cat[Status_cat["Status"]=="Shipped - Returning to Seller"]
seller_ship= Status_cat[Status_cat[
    "Status"]=="Shipped - Returning to Seller"].value_counts()
seller_ship_value
#checking out service level
Service_level = amz["ship-service-level"].value_counts().reset_index()
Service_level_by_date= amz.groupby(["Date"])[
    "ship-service-level"].value_counts().reset_index()
print(tottal_v_of_s)