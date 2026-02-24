import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn-v0_8")
sns.set_palette("Set2")
pd.set_option("display.max_columns",None)
df = pd.read_csv("D:/Projects/world_trade_growth_clean.csv")  
df.head()
print("shape:", df.shape)
df.info()
df.describe()
print("Missing value:\n",df.isnull().sum())
df.columns= df.columns.str.strip().str.lower()
df.drop_duplicates(inplace=True)
df["year"]=df["year"].astype(int)
df.head()
plt.figure(figsize=(10,6))
global_growth= df.groupby("year")["trade_growth_rate"].mean()
print(global_growth.head(10))
plt.plot(global_growth.index, global_growth.values,marker= "o")
plt.title("Global Average trade Growth over time")
plt.xlabel("Year")
plt.ylabel("Average Trade Growth rate (%)")
plt.show()
gb= global_growth.index,global_growth.values.mean()
gb
top_country = (
    df.groupby("country_name")["trade_growth_rate"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
top_country
plt.figure(figsize=(10,6))
sns.barplot(x= top_country.values,
            y= top_country.index)
plt.title("Top 10 countries by average Trade GRowth")
plt.xlabel("Average growth (%)")
plt.ylabel("Top Countries")
plt.show()

region_growth = (
    df.groupby("region")["trade_growth_rate"]
    .mean()
    .sort_values(ascending=False)
)
region_growth
plt.Figure(figsize=(10,6))
sns.barplot(x= region_growth.values,
            y= region_growth.index)
plt.title("average Trade growth by region")
plt.xlabel("Average Growth (%)")
plt.ylabel("region")
plt.show()

income_growth = (
    df.groupby("income_group")["trade_growth_rate"]
      .mean()
      .sort_values(ascending= False)
)
income_growth
plt.figure(figsize=(10,6))
sns.barplot(x= income_growth.index,
            y= income_growth.values
            )
plt.title("Tarde growth by income group")
plt.ylabel("Average grouth(%)")
plt.xticks()
plt.show()
volatility = (
    df.groupby("country_name")["trade_growth_rate"]
    .std()
    .sort_values(ascending=False)
    .head(10)
)
volatility

plt.figure(figsize=(10,6))
sns.barplot( x= volatility.index,
             y= volatility.values)
plt.title("Most volatile countries (trade growth)")
plt.xlabel("standard deviation")
plt.ylabel("country")
plt.xticks()
plt.show()

period_analysis = (
    df.groupby("period")["trade_growth_rate"]
    .mean()
    )
period_analysis

plt.figure(figsize=(10,6))
sns.barplot(x= period_analysis.index,
            y= period_analysis.values)
plt.title("trade growth crisis vs reovery")
plt.xticks(rotation=30)
plt.ylabel("average groth (%)")
plt.show()

plt.Figure(figsize=(6,5))
numeic_cols= df.select_dtypes(include=np.number)
sns.heatmap(numeic_cols.corr(),annot=True,cmap="coolwarm")
plt.title("correlation heatmap")
plt.show()