import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
file=  r"C:\Users\admin\OneDrive\Desktop\Total.csv"
my_file = pd.read_csv(file)
my_file.dropna(inplace= True)
my_file[my_file.isnull().any(axis = 1)]
my_file.head(10)
job_base= my_file[
    "JobTitle"
].value_counts().reset_index()
job_base
x= job_base["JobTitle"].head(10)
y= job_base["count"].head(10)
plt.figure(figsize=(10,3))
plt.title("job base employee count")
plt.plot(x,y,color= "r",
         marker=("o"),
         markerfacecolor= "g",
         linestyle="--",
         linewidth=2,
         markersize=8,
         label="employee count by Job Title")

for d, value in enumerate(y):
    plt.text(
        d,value,str(value),ha= "center",va= "bottom")
plt.xticks(rotation='vertical')
plt.legend(loc="upper right")
plt.xlabel("job title")
plt.ylabel("count of person on job bsae")
plt.grid()
plt.show()
my_file["BasePay"].isnull().sum()
my_file["BasePay"]= pd.to_numeric(
    my_file["BasePay"], errors= "coerce")
my_file.head()
e_j_b= my_file[["EmployeeName","JobTitle","BasePay"]].sort_values(
    by= "BasePay",ascending=False)
e_j_b[e_j_b["BasePay"].isna()]["BasePay"]
e_j_b.dropna(inplace=True)
e_j_b
x_value= e_j_b["EmployeeName"].head(10)
y_value= e_j_b["BasePay"].head(10)
legend= e_j_b["JobTitle"].head(10)
plt.figure(figsize=(20,15))
plt.title("top_salary_based_on_job_role")
plt.bar(x_value,
        y_value,0.5,
        color= "skyblue")
for x, value in enumerate(y_value):
    plt.text(x, value,str(value),ha= "center")
plt.xlabel("empplyee name")
plt.legend("employee name")
plt.xticks(rotation= "vertical", fontsize= 10)
plt.legend(legend)
plt.show()
my_file.head()
my_file["OvertimePay"]= pd.to_numeric(
    my_file["OvertimePay"],errors="coerce")
my_file["OtherPay"]= pd.to_numeric(
    my_file["OtherPay"],errors="coerce")
my_file["TotalPay"]= pd.to_numeric(
    my_file["TotalPay"],errors= "coerce")
my_file["TotalPayBenefits"]= pd.to_numeric(
    my_file["TotalPayBenefits"],errors="coerce")
my_file["Year"]= pd.to_datetime(
    my_file["Year"],errors="coerce")
my_file.dtypes

top_10 = my_file.groupby(
    "EmployeeName")[
        "OtherPay"].sum(

        ).sort_values(
            ascending=False).reset_index(

            ).head(10)
bottom_10= my_file.groupby(
    "EmployeeName")["OtherPay"].sum(

    ).sort_values(
        ascending=False).reset_index(

        ).tail(10)
emp= top_10["EmployeeName"]
highest_p= top_10["OtherPay"]
lowst= bottom_10["OtherPay"]
plt.figure(figsize=(10,5))
high_p_v= np.arange(len(emp))
lowest_p_v= high_p_v + 0.4
for f ,value in enumerate(highest_p):
    plt.text(
        f,value,str(
            value),ha= "center",va= "bottom")
for g, value in enumerate(lowst):
    plt.text(g , value, str(value),ha="center", va="bottom")
plt.bar(high_p_v,
        highest_p,0.3,
        label="top 10 highest_value",
        color= "g")
plt.plot(lowest_p_v,
        lowst,0.3,
        label="10 bottom value",
        color= "r")
plt.xticks(rotation="vertical")
plt.legend("hihest and lowest value")
plt.show()
my_file.head()
my_file["total_pay_of ot_and other_pay"]= my_file[
    "OvertimePay"]+my_file["OtherPay"]
my_file["Years"]= pd.to_datetime(
    my_file["Year"]).dt.year
year_vise_total= my_file.groupby(
    "Years")[
        "total_pay_of ot_and other_pay"].sum(

        ).sort_values(
            ascending= False).reset_index()
year_vise_total
years= year_vise_total["Years"]
value= year_vise_total["total_pay_of ot_and other_pay"]
plt.figure(figsize=(10,6))
plt.stem(years,
        value,
        basefmt="k-",
        linefmt="k-",
        markerfmt="ko",
        label="total pay")
for years ,value in zip(years,value):
    plt.text(years, value, f'{value:.2e}', ha='left', va='bottom', fontsize=10)
plt.title("total pay of over year")
plt.xlabel("years")
plt.ylabel("total of over the year")
plt.xticks(rotation= "vertical")
plt.legend()
plt.grid(True)
plt.show()
year_vise_total
my_file.head(10)
p_or_np= my_file.groupby(
    "Benefits")[
        "TotalPay"].sum(

        ).sort_values(
            ascending= False).reset_index().head(10)
p_or_np
x_value= p_or_np["Benefits"].astype(str)
y_value= p_or_np["TotalPay"]
plt.figure(figsize=(10,6))
plt.stem(x_value,
         y_value,
         basefmt="k-",
         linefmt="b-",
         markerfmt="bo",
         label="total pay benifits")
for x, y in zip(x_value,y_value):
    plt.text(x,y,
             f"{y:.2e}",
             ha="left",
             va= "bottom",
             fontsize= 10)
plt.title("total pay of benifits")
plt.grid(True)
plt.xlabel("benifts_name")
plt.ylabel("benifits pay")
plt.legend()
plt.show()