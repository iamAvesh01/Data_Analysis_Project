import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data= "C:\\Users\\admin\\OneDrive\\Desktop\\python day 24 Your Career Aspirations of GenZ.csv"
netflix= pd.read_csv(data)                          
print(netflix.head())
print(netflix.columns)
#what is the analysis of cuntry?
country= netflix["Your Current Country."].value_counts()
print(country)
label= country.index
count= country.values
colors= ["red","lightgreen"]
#cretaing a  pie usung go.pie fincton
fig = go.Figure(data =[go.Pie(labels= label,
                              values= count)])
#updating figure title using update layout function
fig.update_layout(title_text= "curent country")
fig.update_traces(hoverinfo= "label+value",
                  textinfo = "percent",
                  textfont_size =  30,
                  marker= dict(colors =colors,
                               line= dict(color= "black",
                                          width= 3)))
fig.show()
#factpr infulencing career insprintion
question = netflix["Which of the below factors influence the most about your career aspirations ?"]
question
N_label = question.index
N_value = question.values
N_color = ["gold","lightgreen"]
N_figure = go.Figure(data= [go.Pie(labels= N_label,
                              values= N_value)])
N_figure.update_layout(title_text= "factor infulening career aspriation")
N_figure.update_traces(hoverinfo= "label+value",
                       textinfo= "percent",
                       textfont_size=   30,
                       marker= dict(colors= N_color,
                                    line= dict(color= "black",
                                               width= 3)))
N_figure.show()
question2= "Would you definitely pursue a Higher Education / Post Graduation outside of India ? If only you have to self sponsor it."
question2= netflix[question2].value_counts()
question2
able= question2.index
acnt= question2.values
aclr= ["orange","black"]
afig= go.Figure(data= [go.Pie(labels= able,
                             values= acnt)])
afig.update_layout(title_text= "who is intrested")
afig.update_traces(hoverinfo= "label+value",
                   textinfo= "percent",
                   textfont_size= 30,
                   marker=  dict(colors= aclr,
                                 line= dict(color= "black",
                                            width= 3)))
afig.show()
#whpo are intrested to do work in out side of india three year
ques1= "How likely would you work for a company whose mission is misaligned with their public actions or even their product ?"
ques1= netflix[ques1].value_counts()
ques1
P_label = ques1.index
P_values = ques1.values
P_figure = go.Figure(data= [go.Pie(labels= P_label,
                                   values= P_values)])
P_figure.show()
P_figure.update_traces(hoverinfo= "label+value",
                       textfont_size= 25,
                       marker=  dict(colors= ["red","green"],
                                     line= dict(color= "black",
                                                width=  3)))
P_figure.show()
#create a pie chart for that
#What is the most preferred working environment for you.
qu2= "What is the most preferred working environment for you."
qu2= netflix[qu2].value_counts()
qu2
que2= go.Figure(data= [go.Pie(labels= qu2.index,
                              values= qu2.values)])
que2.update_layout(title_text="what is tthe most preferred working inviromentt for you")
que2.update_traces(hoverinfo= "label+value",
                   marker= dict(colors= ["blue","lightgreen","red","yellow","orange","purple"],
                                line= dict(color= "red",
                                           width= 2)))
que2.show()