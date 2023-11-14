#importing libarary for project
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os 
import numpy as np
import matplotlib.pyplot as plt
#file path
path = r"C:\Users\admin\OneDrive\Desktop\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"
all_file = [file for file in os.listdir(path)]
#merge all file in one csv file
all_data = pd.DataFrame()
for file in all_file:
    data_f = pd.read_csv(os.path.join(path,file))
    all_data= pd.concat([all_data,data_f])

#save the merged data to a new csv file
all_data.to_csv("all_data.csv",index= False)
# finding the missing value in data
all_data[
    all_data.isnull(

    ).any(
        axis= 1)
        ]
# droping the missing data
all_data.dropna(inplace=True)
#checking again missing data
all_data[
    all_data.isnull(

    ).any(
        axis= 1
    )
]
#adding the month column
all_data["Month"] = None
all_data["Month"] = all_data["Order Date"].str[0:2]
#find or and delete
all_data = all_data[all_data["Order Date"].str[0:2] != "Or"]
month_map= {'01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'}
all_data["Month"]= all_data["Month"].map(month_map)
all_data
# converting data type of month column

#searching the data or in order date 
#all_data[all_data["Order Date"].str.contains("Or", case= True, na= False)]
all_data.head()
#converting the data type 
all_data[
    "Quantity Ordered"
    ]= pd.to_numeric(all_data[
        "Quantity Ordered"
        ])

all_data[
    "Quantity Ordered"
    ].dtype
all_data[
    "Price Each"
    ]= pd.to_numeric(all_data[
        "Price Each"
        ])
all_data["Price Each"].dtype
all_data["sales"]= all_data["Quantity Ordered"]*all_data["Price Each"]
highest_earn =all_data.groupby("Month")[["Quantity Ordered","Price Each", "sales"]].sum().reset_index()
highest_earn["sales"]= pd.to_numeric(highest_earn["sales"])
highest_earn.dropna(inplace= True)
#ceating a bar figure
import plotly.graph_objects as go

# Create a list of months and sales values
months = highest_earn["Month"]
sales = highest_earn["sales"]

# Create a bar trace for each month with a legend label
traces = []
for month, sales_value in zip(months, sales):
    trace = go.Bar(
        x=[month],
        y=[sales_value],
        name=month
    )
    traces.append(trace)

# Create the figure with all the bar traces
month_bar = go.Figure(data=traces)

# Set the title of the figure
month_bar.update_layout(
    title="Highest Sales by Each Month",
    paper_bgcolor= "black",
    plot_bgcolor="white",
    font= dict(
        color= "white"
    )
)

# Set showlegend to True to display the legend
month_bar.update_layout(showlegend=True)
month_bar.show()
#creating scatter plot using plotly
scatter_h= go.Figure(
    data= [
        go.Scatter(
            x= highest_earn["Month"],
            y= sales,
            name= "Month"
        )
    ]
)
scatter_h.update_layout(
    title= "sales per month",
    showlegend= True,
    xaxis_title= "Month",
    yaxis_title= "Value per month",
    paper_bgcolor= "black",
    plot_bgcolor= "white",
    font= dict(
        color= "white"
    )
)
scatter_h.show()
# creating pie chart useing plotly
pie_chart_h = go.Figure(
    data= [
        go.Pie(
            labels= highest_earn["Month"],
            values= highest_earn["sales"],
            name= "Month"
        )
    ]
)
pie_chart_h.update_layout(
    title= "sales per month",
    showlegend= True,
    xaxis_title= "Month",
    yaxis_title= "Value per month",
    paper_bgcolor= "black",
    plot_bgcolor= "white",
    font= dict(
        color= "white"
    )
)
pie_chart_h.show()
#creating donut chart using plotly
donut_h= go.Figure(
    data= [
        go.Pie(
            labels= highest_earn["Month"],
            values= highest_earn["sales"],
            name= "MOnth",
            hole= 0.4
        )
    ])
donut_h.update_layout(
    title= "sales per month",
    showlegend= True,
    paper_bgcolor= "black",
    plot_bgcolor= "white",
    font= dict(
        color= "white"
    )

)

donut_h.show()
# creating scatter bubule plot
bubble_h= go.Figure(
    data= [go.Scatter(
        x= highest_earn["Month"],
        y= highest_earn["sales"],
        name= "Month",
        mode= "markers",
        marker= dict(
            size= [size / max(sales)* 40 for size in sales],
            sizemode= "diameter",
            color = "turquoise"          
        )
    )]
)
bubble_h.update_layout(
    title= "Sales per Month",
    showlegend= True,
    )
bubble_h.show()
#  get the hiest sales each city
#  add the city column
#  using apply function
def get_city(address):
    return address.split(",")[1]
def get_state(address):
    return address.split(",")[2].split(" ")[1]
all_data["City"] = all_data["Purchase Address"].apply(lambda x : f"{get_city(x)}({get_state(x)})")
highest_sale_city= all_data.groupby("City")["sales"].sum().reset_index()
highest_sale_city
#creating bar grpah
city= highest_sale_city["City"]
sales= highest_sale_city["sales"]
traces= []
for city ,sales_value in zip(city,sales):
    trace= go.Bar(
        x= [city],
        y = [sales_value],
        name= city
    )
    traces.append(trace)
city_bar=  go.Figure(data= traces)
city_bar.update_layout(
    showlegend= True
)
city_bar.show()
#what time should we display advertisment to maxmize liklihood of  customer buying product
all_data["Order Date"].info
# convert datetime formet
all_data["Order Date"]= pd.to_datetime(all_data["Order Date"])
all_data["Order Date"].info
# adding the hour coloumn
all_data["hour"]= all_data["Order Date"].dt.hour
#adding the miniute column
all_data["minute"]= all_data["Order Date"].dt.minute
# adding the count colummn
all_data["count"]= all_data["count"]=1
all_data.head()
hour_per_sale = all_data.groupby(
    "hour"
    )[
        "sales"
        ].sum().reset_index()
hour_per_sale
hour= [hour for hour,
       df in hour_per_sale.groupby("hour")]
plt.plot(hour,
         hour_per_sale.groupby(["hour"]).count())
plt.xticks(hour)
plt.title("sales per hour")
plt.xlabel("hour")
plt.ylabel("sales per hour")
plt.grid()
plt.show()