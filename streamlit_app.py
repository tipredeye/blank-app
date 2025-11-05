import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import gspread

#page setup
st.set_page_config(layout="wide")
st.title("12 signs of the zodiac")
st.write(pd.DataFrame({
    'Sign_ID': ["Aries","Taurus","Gemini","Cancer",
                "Leo","Virgo","Libra","Scorpio",
                "Sagittarius","Capricorn","Aquarius","Pisces"],
    'Elements': ["Fire","Earth","Air","Water",
                 "Fire","Earth","Air","Water",
                 "Fire","Earth","Air","Water",
                 "Fire","Earth","Air","Water"]
}))

array1= ["Aries","Taurus","Gemini","Cancer",
         "Leo","Virgo","Libra","Scorpio",
         "Sagittarius","Capricorn","Aquarius","Pisces"]
array2= ["Fire","Earth","Air","Water",
         "Fire","Earth","Air","Water",
         "Fire","Earth","Air","Water",
         "Fire","Earth","Air","Water"]
if len("array1") == len("array2"):
        df= pd.DataFrame({'Sign_ID':array1,'Elements':array2})
