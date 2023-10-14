import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data = r"C:\Users\admin\OneDrive\Desktop\IPL_2022.csv"
data1 = pd.read_csv(data)
print(data1)

figure = px.bar(data1, x=data1["match_winner"],
                title="Number of matches won in 2022")

data1["won_by"] = data1["won_by"].map({"wicket": "chasing",
                                       "runs": "defending"})
won_by = data1["won_by"].value_counts()
label = won_by.index
counts = won_by.values
color = ["red", "lightgreen"]

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Number of matches won by defending vs. chasing")

fig.update_traces(hoverinfo="label+percent",
                  textinfo="value", textfont_size=30,
                  marker=dict(colors=color, line=dict(color="black", width=3))
                 )

fig.show()
figure1= px.bar(data1, x= data1["best_bowling"],
                title= "best bolwer in ipl 2022")

figure1.show()
figure2= px.bar(data1, x= data1["player_of_the_match"],
                title= "man of the match player in ipl 2022")
figure2.show()
figure3= px.scatter(data1, x = "team1",
                    y= "won_by",
                    size="first_ings_score",trendline="ols",
                    title="Team 1 won by highest margin")
figure3.show()
color= ["red","lightgreen"]
import plotly.express as px 
fig = px.pie(data1, names="match_winner",
             values="highscore",
             title= "match winner name of highest score")
fig.show()
figure4 = go.Figure(data=[go.Pie(labels=data1["team1"],
                                 values=data1["first_ings_score"],
                                 title="team 1 fist enning score")])
figure4.show()
figure5 = px.bar(data1,
                 x= data1["top_scorer"],
                 y= data1["highscore"],
                 color= data1["highscore"],
                 title= "top highscor in IPL 2022")
figure5.show()