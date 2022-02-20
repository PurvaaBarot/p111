import plotly_express as px
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import pandas as pd
import random
import statistics

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

print("Mean = " , mean)
print("STD = " , std)

def generate_sample_mean(counter):
    sample=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        sample.append(value)

    sample_mean=statistics.mean(sample)
    return sample_mean

mean_list = []

for i in range(0,1000):
    sample_mean=generate_sample_mean(100)
    mean_list.append(sample_mean)

mean_of_sample_mean=statistics.mean(mean_list)
std_of_sample_mean=statistics.stdev(mean_list)

print("mean of sample mean = " , mean_of_sample_mean)
print(" std of sample mean = " , std_of_sample_mean)

std_start1, std_end1 =mean-std_of_sample_mean , mean+std_of_sample_mean
std_start2, std_end2 =mean-2*std_of_sample_mean , mean+2*std_of_sample_mean
std_start3, std_end3 =mean-3*std_of_sample_mean , mean+3*std_of_sample_mean

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

mean = statistics.mean(data)
std = statistics.stdev(data)

fig=ff.create_distplot([mean_list] , ["Claps"] , show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean] , y=[0,0.01] , mode="lines" , name="Mean"))
fig.add_trace(go.Scatter(x=[mean,mean] , y=[0,0.01] , mode="lines" , name="Mean"))
fig.add_trace(go.Scatter(x=[std_end1,std_end1] , y=[0,0.01] , mode="lines" , name="First std end"))
fig.add_trace(go.Scatter(x=[std_end2,std_end2] , y=[0,0.01] , mode="lines" , name=" Second std end"))
fig.show()

print("Mean = " , mean)
print("STD = " , std)

mean_of_sample1 = statistics.mean(data)

z=(mean_of_sample1-mean)/std_of_sample_mean
print(z)