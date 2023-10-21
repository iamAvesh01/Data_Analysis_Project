import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data= r"C:\Users\admin\OneDrive\Desktop\Netflix.csv"
df = pd.read_csv(data)
df.head()
sns.set(rc={"figure.figsize":(10,5)})
df["Date"]= pd.to_datetime(df["Date"])
df1= df.set_index(df["Date"])
print(df1.head())
sns.lineplot(x= df1.index,
             y= df1["Volume"],
             label= "Volume")
plt.title("Volume of stock versos time")
df.plot(y=["High","Close","Open"],
        title= "netflix stock price")
fig,(ax1,ax2,ax3)=plt.subplots(3,figsize = (15,10))
df1.groupby(df1.index.day).mean().plot(y="Volume",
                                       ax= ax1, xlabel= "Day")
df1.groupby(df1.index.month).mean().plot(y= "Volume",
                                         ax= ax2,xlabel="Month")
df1.groupby(df1.index.year).mean().plot(y= "Volume",
                                        ax= ax3,
                                        xlabel="Year")
ad= df1.sort_values(by= "High",
                    ascending = False).head(5)
print(ad)
ad1= df1.sort_values(by="Low",
                     ascending= True).head(5)
print(ad1)
fig,axes = plt.subplots(nrows=1,
                        ncols=2,
                        sharex = True,
                        figsize =(12,5))
fig.suptitle("high & Low value stock per period of time",fontsize = 18)
sns.lineplot(ax= axes[0],
             y= df1["High"],
             x= df1.index,
             color="green")

sns.lineplot(ax= axes[1],
             y= df1["Low"],
             x= df1.index,
             color= "red")
