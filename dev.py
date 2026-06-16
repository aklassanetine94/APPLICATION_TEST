# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:15:29 2022

@author: Acer
"""
#####################################
import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module


#####################################










import pandas as pd 
from PIL import Image
import math 
import streamlit as st
#from PIL import image

df=pd.read_csv(r"C:/Users/Acer/Downloads/Maladies_cardiaques1.csv")

#st.title(":bar_chart: Sales Dashboard")
from PIL import Image
groupama=Image.open("C:/Users/Acer/Downloads/Groupama.png")

name="Alassane TINE"
describe="Je suis etudiant en master 1 data science"
email="a.alassane.tine@gmail.com"
phone="07 58 95 41 03"
#col1, col2= st.columns(2, gap="small")#[3, 1]

from PIL import Image
groupama=Image.open("C:/Users/Acer/Downloads/Groupama.png")
col1, col2= st.columns([1,3])
with col1:
    st.image(groupama, width=230)
   #st.header("A cat")
   #st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.title(":bar_chart: Sales Dashboard")
    st.write(name)
    #st.write(describe)
    #st.write(email, phone)
   #st.header("A dog")
   #st.image("https://static.streamlit.io/examples/dog.jpg")



    st.write(describe)
    st.write(email, phone)
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")




 
 
    
st.markdown("##")
total_sales = int(df["Age"].sum())
average_rating = round(df["RestingBP"].mean(), 1)
#star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df["Age"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Vente total:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Note moyen:")
    st.subheader(f"{average_rating:,}" )  
with right_column:
    st.subheader("vente moyenne par transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")





import plotly.express as px
st.markdown("""---""")

# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    df.groupby(by=["RestingECG"]).sum()[["Age"]].sort_values(by="Age")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Age",
    y=sales_by_product_line.index,
    #orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



sales_by_hour = df.groupby(by=["ChestPainType"]).sum()[["Age"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Age",
    #orientation="h",
    title="<b>Sales by hour</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)
fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)




left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)


st.write(df)

#df = pd.read_csv(data_file)
#st.dataframe(df)




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))


option2 = st.selectbox(
    'How would you like to be contacted?',
    ('Email2', 'Home phone2', 'Mobile phone2'))

st.write('You selected:', option)
st.write('You selected:', option2)

 
   
   
   
   