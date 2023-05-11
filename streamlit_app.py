import streamlit 
import pandas as pd 

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Brek Menu")
streamlit.text("🥣 food")
streamlit.text("🥗 food")
streamlit.text("🐔 food")
streamlit.text("🥑🍞 food")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
