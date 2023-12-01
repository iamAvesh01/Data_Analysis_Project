import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly_express as px
import matplotlib.pyplot as plt
file_path = r"C:\Users\admin\OneDrive\Desktop\crime.csv"
c_data= pd.read_csv(file_path,encoding="latin-1")
c_data[c_data.isnull().any(axis=1)]
c_data.dtypes
c_data[c_data.dropna()]
c_data.head(20)
dpl= c_data.duplicated()
unq= c_data.stack().unique()
c_data["first_occurrence_date"]= pd.to_datetime(
    c_data["first_occurrence_date"]
)
c_data["last_occurrence_date"]= pd.to_datetime(
    c_data["last_occurrence_date"]
)
c_data["reported_date"]= pd.to_datetime(
    c_data["reported_date"]
)
c_data.dtypes
c_data.drop("Unnamed: 18",axis=1, inplace=True)
c_data[c_data.isna().any(axis=1)]
c_data.dropna(axis=1)
c_data.drop("last_occurrence_date",
            axis=1,
            inplace= True)
o_t_i= c_data.groupby("offense_category_id"
                      )["is_crime"].sum(
                          
                      ).sort_values(ascending=True).reset_index()
o_t_i
oti_ID= o_t_i["offense_category_id"]
oti_crime= o_t_i["is_crime"]
o_t_i_P= go.Figure(
    data=[go.Pie(
        labels= oti_ID,
        values= oti_crime        
    )]
)
o_t_i_P.update_layout(title_text= "Total crime by category",
                      font= dict(
                          size= 18,
                          color="white"
                      ),
                      paper_bgcolor="black")
o_t_i_P.update_traces(
    marker= dict(
        line=dict(
            color= "white",
            width=1.5
        )
    )
)
o_t_i_P.show()
def extract_cities(address):
    if isinstance(address,str):
      add_part= address.split(" ")
      if len(add_part)>1:
         return add_part[1:]
      else :
         return None
    else:
       return None
c_data["crime_address"]= c_data["incident_address"].apply(extract_cities)
c_data["crime_address"]= c_data["crime_address"].astype("object")
C_C_A= c_data[["first_occurrence_date","is_crime","crime_address"]]
C_C_A["first_occurrence_Year"]= C_C_A["first_occurrence_date"].dt.year
C_C_A["crime_address"]= C_C_A[
   "crime_address"].apply(lambda x: str(x))
C_C_A= C_C_A.groupby(
   "first_occurrence_Year")[
      "is_crime"
      ].sum().sort_values(
         ascending= True
         ).reset_index()


label1 = C_C_A["first_occurrence_Year"]
value1 = C_C_A["is_crime"]
traces = []

for label, value in zip(label1, value1):
    trace = go.Bar(
        x=[label],
        y=[value],
        name=str(label)
    )
    traces.append(trace)

bar_graph = go.Figure(data=traces)

bar_graph.update_layout(
    title="Total Crime by each year",
    paper_bgcolor="black",
    font=dict(
        color="white"
    )
)

bar_graph.update_layout(
    showlegend=True
)

# Use plotly.offline.plot if running in a non-interactive environment
bar_graph.show()
C_C_A.head()

c_data.head()
c_data[
      "first_occurrence_date_YEAR"
   ]= c_data[
      "first_occurrence_date"].dt.year
c_data.head()
total_victim= c_data.groupby(
   "first_occurrence_date_YEAR")[
      "victim_count"].sum().sort_values(ascending= False).reset_index()
total_victim
C_C_A.head()

fig= plt.figure()
ax= fig.add_axes([0,0,1,1])
l1= ax.plot(
    total_victim["first_occurrence_date_YEAR"],
    total_victim["victim_count"],
    "ys-"
)
l2= ax.plot(
    C_C_A["first_occurrence_Year"],
    C_C_A["is_crime"],
    "go--"
)
ax.legend(
    labels= ("total crime by year","total victim by year")
)
ax.set_title("victim and crime by each year")
ax.set_xlabel("year's count")
ax.set_ylabel("values")
plt.show()
c_data.head()
offsens_by_year= c_data["first_occurrence_date_YEAR"].value_counts().reset_index()
offsens_by_year
x1= offsens_by_year['first_occurrence_date_YEAR']
y1= offsens_by_year["count"]
traces1= []
for label, value in zip(x1,y1):
    lineplot= go.Waterfall(
        x= x1,
        y= y1,
        base= 200
    )
    traces1.append(lineplot)
wtr_fll = go.Figure(data= traces1)
wtr_fll.update_layout(title= "total distribution of year",
)
wtr_fll.show()
c_data.head()
nighbr= c_data["neighborhood_id"].value_counts().reset_index()
nighbr
y_label= nighbr["neighborhood_id"]
x_count= nighbr["count"]
traces3=[]
for y3,x3 in zip (y_label,x_count):
    fnnl= go.Funnel(
        y= [y3],
        x= [x3]
    )
    traces3.append(fnnl)

f_fig= go.Figure(traces3)
f_fig.update_layout(title_text= "The Count of nigheborhood ",
                    xaxis_title= "total count",
                    yaxis_title= "nigheborhood names",
                    font=dict(
                       size= 14,
                       color= "red"
                    ),
                    plot_bgcolor= "lightgrey")
f_fig.show()
c_data.head() 
id_type= c_data["offense_type_id"].value_counts().reset_index().head(10)
id_type
ax1= id_type["offense_type_id"]
ay1= id_type["count"]
trac12= []
for nn, mm in zip(ax1,ay1):
   trac32= go.Scatter3d(x= [nn],
                      y= [mm],
                      z=[0],
                      mode= "markers")
   trac12.append(trac32)
sc1= go.Figure(trac12)
sc1.update_layout(title_text=" Total crime type count",
                  xaxis_title= "Type id ",
                  yaxis_title="value of total type id",
                  font= dict(
                     size= 14,
                     color="grey"
                  )
                  )
sc1.show()
c_data.head(20)
off_code= c_data["offense_code"].value_counts().reset_index()
off_code
a1= off_code["offense_code"].head(20).tolist()
b1= off_code["count"].head(20).tolist()
name= off_code["offense_code"].head()
sc1= []
for x_list,y_list in zip(a1,b1):
   tr= go.Scatter(x= [x_list],
                  y= [y_list])
   sc1.append(tr)
sc_fig = go.Figure(sc1)
sc_fig.update_layout(title_text= "Total count of offense code")
sc_fig.show()
c_data.head()

distribution= c_data.groupby(
   "offense_code_extension"
   ).agg(
      {
         "victim_count": "mean",
         "is_crime" : "mean"}).reset_index()

c_data.head()
dts_geo = c_data["geo_x"].value_counts(
   
).reset_index().max()
dts_geo
dts_geo1 = c_data["geo_x"].value_counts(
   
).reset_index().min()
dts_geo1
dts_geo2 = c_data["geo_x"].value_counts(
   
).reset_index().head(20)
dts_geo2
d_xlis= dts_geo2["geo_x"].head(20).tolist()
d_ylis= dts_geo2["count"].head(20).tolist()

d_trace= []
for x_d_lis, y_d_ylis in zip(d_xlis,d_ylis):
   dt= go.Scatter(x= [x_d_lis],
                  y= [y_d_ylis],
                  error_y= dict(
                     type= "data",
                     symmetric= False,
                     array=[0.1,0.2,0.1,0.1],
                     arrayminus=[0.2,0.4,1,0.2]
                  ),
                  )
   d_trace.append(dt)
d_tr_f= go.Figure(d_trace)
d_tr_f.update_layout(title_text= "geogrphcial total count")
d_tr_f.show()
distribution
dt_xlis= distribution["offense_code_extension"].head(100).tolist()
dt_ylis= distribution["victim_count"].head(100).tolist()
dt_name= distribution["is_crime"].head(100).tolist()
dt_tr= []
for dtx_lis, dty_lis in zip (dt_xlis,dt_ylis):
   adr= go.Heatmap(x= [dtx_lis],
                   y= [dty_lis],
                   z= [dt_name ]
                   )
   dt_tr.append(adr)
dst_fig= go.Figure(dt_tr)
dst_fig.update_layout(title_text= "total distributionof  is crime and total victim")
dst_fig.show()
dts_geo2
geo_x= dts_geo2["geo_x"].tolist()
geo_y= dts_geo2["count"].tolist()
geo= []
for geo_xlis, geo_ylis in zip(geo_x,geo_y):
   geo_g= go.Contour(x= [geo_xlis],
                 y= [geo_ylis],
                 z= [geo_xlis]
                 )
   geo.append(geo_g)
geo_fig = go.Figure(geo)
geo_fig.update_layout(title_text= "the tatal value of geo X")
geo_fig.show()