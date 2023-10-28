import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
data= r"C:\Users\admin\OneDrive\Desktop\hotel_booking.csv"
hotel_data = pd.read_csv(data)
hotel_data.head()

hotel_data.shape
hotel_data.columns

hotel_data[
    "reservation_status_date"
    ]= pd.to_datetime(
        hotel_data[
            "reservation_status_date"
            ])
hotel_data.dtypes
hotel_data.describe(
    include= 'object'
    ) # for showing object value

for col in hotel_data.describe(
    include= 'object'
    ).columns:
    print(col)
    print(hotel_data[col].unique())
    print("-"*50)
hotel_data.isnull().sum()
 
hotel_data.drop(
    [
        'agent','company'
        ],axis = 1 ,
        inplace= True 
        )

hotel_data.dropna(
    inplace= True
    )
hotel_data.isnull().sum() #checking missing value again
hotel_data =hotel_data[
    hotel_data[
        'adr'
        ]<5000] # removing oulaires adr grater then 5000
hotel_data.describe()

cancelled_perc= hotel_data[
    "is_canceled"
    ].value_counts(
        normalize= True
        )
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title(
    "Rservation status count"
    )
plt.bar(
    [
        "Not canceled","Canceled"
        ],
        hotel_data[
            "is_canceled"
            ].value_counts(),
        edgecolor = "k",
        width = 0.3)
plt.show()
plt.figure(
    figsize= (8,4)
    )
ax1 = sns.countplot(
    x = "hotel",
    hue = "is_canceled",
    data= hotel_data,
    palette = "Blues")
legend_labels = ax1.get_legend_handles_labels()
ax1.legend(
    legend_labels[0],[
        "Not Canceled","Canceled"
        ],
           title="resveration status",
           bbox_to_anchor= (1,1))
plt.title(
    "reseveration status in diffrent hotels"
    )
plt.xlabel(
    "hotel"
    )
plt.ylabel(
    "number of resveration"
    )
plt.show()
resort_hotel_p = hotel_data[
    hotel_data[
        "hotel"]
        == "Resort Hotel"]
resort_hotel_p[
    "is_canceled"
    ].value_counts(
        normalize =True
        )
print(
    resort_hotel_p
    )
city_hotel_p = hotel_data[
    hotel_data[
        "hotel"]
        == "City Hotel"]
canl_of_city_p= city_hotel_p[
    "is_canceled"
    ].value_counts(
        normalize = True
        )
print(canl_of_city_p)
print(canl_of_city_p)
hotel_data.head()
rhp = resort_hotel_p.groupby(
    "reservation_status_date")[
        ["adr"]
        ].mean()
chp = city_hotel_p.groupby(
    "reservation_status_date"
    )[
        ["adr"]
        ].mean()
plt.figure(figsize= (20,8))
plt.title("Avaarage daily rate in city and resort hotel")
plt.fontsize=30
plt.plot(rhp.index,
         rhp["adr"],
         label= "resort_hotel"
         )
plt.plot(chp.index,
         chp["adr"],
         label= "city_hotel"
         )
plt.legend(fontsize=20)
plt.show()

hotel_data_d =  hotel_data["month"]= hotel_data[
    "reservation_status_date"
    ].dt.month
print(hotel_data_d)
plt.figure(figsize= (16,8))
ax3 = sns.countplot(x = "month",
                    hue= "is_canceled",
                    data= hotel_data,
                    palette= "bright")
legend_labels_1 = ax3.get_legend_handles_labels()
ax3.legend(bbox_to_anchor= (1,1))
plt.title("resveration status as per month", size = 20)
plt.xlabel("Month status")
plt.ylabel("number of reservation status")
plt.legend(["not canceled","canceled"])
plt.show()

data1 = hotel_data[
    hotel_data[
        "is_canceled"
        ] == (1)].groupby("month")[["adr"]].sum().reset_index()
plt.figure(figsize= (15,8))
plt.title("adr per month",
          fontsize = 30)
sns.barplot( x = "month",
             y = "adr",
            data= hotel_data[
                hotel_data[
                    "is_canceled"
                    ] == (1)].groupby("month")[["adr"]].sum().reset_index())
plt.show()

canceled_data1 = hotel_data[
    hotel_data[
        "is_canceled"
        ]== 1]
top_10_c =canceled_data1[
    "country"
    ].value_counts()[:10]
plt.figure(figsize= (8,8))
plt.pie(top_10_c,
        autopct= "%.2f",
        labels= top_10_c.index)
plt.title("top 10 country resvervatio country")
plt.show()

hotel_data[
    "market_segment"
    ].value_counts(
        normalize= True
        )
canceled_data1[
    "market_segment"
    ].value_counts(normalize= True)

not_canceled_data_1= hotel_data[hotel_data["is_canceled"]== 0]
cancel_hotel_adr = canceled_data1[
    (canceled_data1[
        "reservation_status_date"
        ] >= '2016') & 
                                  (canceled_data1[
                                      "reservation_status_date"
                                      ] <= '2017')]
not_cancel_adr = not_canceled_data_1[
    (not_canceled_data_1[
        "reservation_status_date"
        ] >= '2016') & 
                                     (not_canceled_data_1[
                                         "reservation_status_date"
                                         ] <= '2017')]
plt.figure(figsize= (20,6))
plt.title("Avage daily rate")
plt.plot(cancel_hotel_adr[
    "reservation_status_date"
    ],
         cancel_hotel_adr["adr"], 
         label= "canceled")
plt.plot(not_cancel_adr["reservation_status_date"],
         not_cancel_adr["adr"], 
         label= "not canceled")
plt.legend(fontsize= 20)
