# essential libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb



# function on pandas to read the file of extension .csv 

df = pd.read_csv("data2.csv")

# part 1 make dataframe for countries

cn_df = df["Country Name"]


def convY_df(param):
    lst = list()
    for i in param:
        print(i)
y_df = df.iloc[0:0,4:-1]
years = convY_df(y_df)



df_Bangladesh = df.loc[(df['Country Name'] == "Bangladesh") & (df['Indicator Name'] == "Agricultural land (% of land area)")]


df_bangladesh_pG = df_Bangladesh.iloc[:,5:-1].values



df_bangladesh_pG=df_bangladesh_pG[np.logical_not(np.isnan(df_bangladesh_pG))] 
convData = list(df_bangladesh_pG)  

import plotly.express as px
from matplotlib.pyplot import figure

figure(figsize=(10, 8), dpi=80)


# agriculture land bangladesh
def Ag_hist_banglades():
    # ploting histogram of dataset
    fig = px.histogram(convData,x=years, marginal="rug", nbins = 10)
    fig.show()
Ag_hist_banglades()


# agriculture land canada
def Ag_Hist_Canada():

    # pandas bulitin function
    df_canada = df.loc[(df['Country Name'] == "Canada") & (df['Indicator Name'] == "Agricultural land (% of land area)")]

    # array
    y_df = df_canada.iloc[:,5:-1].values

    # kill null spaces
    df_bangladesh_pG=df_bangladesh_pG[np.logical_not(np.isnan(df_bangladesh_pG))]
    data = list(y_df)

    # making histogram
    fig = px.histogram(data,x = years, nbins = 10,
                      color_discrete_sequence=['indianred'])
    fig.show()
Ag_Hist_Canada()


# agriculture land switzerland
def Ag_Hist_Switzerland():

    # making datset of indicator
    df_Switzerland = df.loc[(df['Country Name'] == "Switzerland") & (df['Indicator Name'] == "Agricultural land (% of land area)")]
    # array of dataset
    y_df = df_Switzerland.iloc[:,5:-1].values

    # kill null
    df_bangladesh_pG=df_bangladesh_pG[np.logical_not(np.isnan(df_bangladesh_pG))]
    data = convertIntoList(y_df)

    # plotting
    fig = px.histogram(data,x = years, nbins = 25,
                      color_discrete_sequence=['green'])
    fig.show()
Ag_Hist_Switzerland()




def combo3():

    # indicator 1
    df_Switzerland = df.loc[(df['Country Name'] == "Switzerland") & (df['Indicator Name'] == "Agricultural land (% of land area)")]
    y_df1 = df_Switzerland.iloc[:,5:-1].values
    y_df1=y_df1[np.logical_not(np.isnan(y_df1))]
    data1 = list(y_df1)


    # indicator 2
    df_canada = df.loc[(df['Country Name'] == "Switzerland") & (df['Indicator Name'] == "Cereal yield (kg per hectare)")]
    y_df2 = df_canada.iloc[:,5:-1].values
    y_df2=y_df2[np.logical_not(np.isnan(y_df2))]
    data2 = list(y_df2)
    
    df_Bangladesh = df.loc[(df['Country Name'] == "Switzerland") & (df['Indicator Name'] == "Urban population (% of total population)")]
    y_df3 = df_Bangladesh.iloc[:,5:-1].values
    y_df3=y_df3[np.logical_not(np.isnan(y_df3))]
    data3 = list(y_df3)
    lstdata = data1[10:20]
    lstdata2 = data2[10:20]
    lstdata3 = data3[10:20]


    # making list by list comprehension
    new2= [i/40 for i in lstdata2]
    # size
    plt.figure(figsize=(13,9))

    # plotting
    n = len(lstdata2)
    r = np.arange(n)
    width = 0.25
    plt.bar(r, lstdata, width, color = 'r')
    plt.bar(r+width, new2, width, color = 'g')
    plt.bar(r+width*2, lstdata3, width, color = 'b')
    plt.xlabel("Year")
    plt.ylabel("indicator")
    plt.title("Number of people voted in each year")

    plt.show()
    
combo3()   




