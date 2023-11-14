import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
diwali = r"C:\Users\admin\OneDrive\Desktop\diwali_4.csv"
d_data = pd.read_csv(diwali)
d_data.shape
d_data.drop(["Status",
              "unnamed1"],
            axis= 1,
            inplace= True)
pd.isnull(
    d_data
    ).sum()
pd.isnull(
    d_data[
        "Amount"
        ]).sum()
d_data.dropna(
    inplace= True)
d_data[
    "Amount"
    ]= d_data[
        "Amount"
        ].astype("int")
d_data[
    "Amount"
    ].dtypes
d_data[
    ["Age","Orders","Amount"]
    ].describe()
gener= d_data[
    "Gender"
    ].value_counts()
plt.figure(figsize=(8,4))
sns.barplot(x= gener.index,
              y= gener.values,
              palette= ["red","green"],
              )
plt.title("total count of gender")
plt.xlabel("gender")
plt.ylabel("count of gender")
plt.legend(title= "gender")
plt.show()
d_data[["Gender","Amount"]]

sales_gen= d_data.groupby(
    ["Gender"],
    as_index= False
    )[
        "Amount"
        ].sum(

        ).sort_values(
            by= "Amount",
            ascending= False)
sales_gen
sales_fig= go.Figure(
    data= [
        go.Pie(
            labels= sales_gen["Gender"],
            values= sales_gen["Amount"]
        )
    ]
)
sales_fig.update_layout(title= "total amount of gender ")
sales_fig.update_traces(
    hoverinfo = "label+value",
    marker= dict(
        colors= ["lightgreen","pink"],
        line= dict(
            color= "black",
            width= 3
        )
    )
)
sales_fig.show()

sales_age=d_data.groupby(
    [
        "Age Group"
    ],
    as_index= False
)["Amount"].sum().sort_values(
    by= "Amount",
    ascending= False
)
sales_age
sales_fig_bar= go.Figure(
    data=[
       go.Bar(
           x= sales_age["Age Group"],
           y= sales_age["Amount"],
           marker=dict(
               color= ["burlywood", "cadetblue",
            "chartreuse", "chocolate", "coral", "cornflowerblue",]
           )
       ) 
    ]
)
sales_fig_bar.show()
d_data.head()
d_data[["Cust_name","Orders","Amount"]]
data_coa= d_data.groupby("Cust_name").agg({"Orders": "sum","Amount": "sum"}).reset_index()
plt.figure(figsize=(10,6))
plt.bar(data_coa["Cust_name"].head(10),
        data_coa["Orders"].head(10),width= 0.35,
        label= "Order",
        color= "blue")
plt.bar(data_coa["Cust_name"].head(10),
        data_coa["Amount"].head(10),width= 0.35,
        label= "Amount",
        color= "orange")
plt.xlabel("custmoer name")
plt.ylabel("total")
plt.title("total order and amount per customer")
plt.legend()
plt.show()
figure_d= go.Figure(
    data=[go.Bar(
        x= d_data["Cust_name"].head(20),
        y= d_data["Orders"].head(20),
        name= "Orders",
        base= "blue"
    )]
)
figure_d.add_trace(
    go.Bar(
        x= d_data["Cust_name"].head(20),
        y= d_data["Amount"].head(20),
        name= "name",
        base= "red"
    )
)
figure_d.show()
d_data.head()
