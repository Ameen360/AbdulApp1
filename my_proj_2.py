import streamlit as st
import pandas as pd


st.set_page_config(page_title="Temperature App",page_icon=":cold_face:")


# --- Title----

st.title("Temperature Conversion App")


Temp = {"Location":[],
            "Value":[]

}

#----- Form -----

with st.form(key="form", clear_on_submit=True):
    Location = st.text_input("Enter your Location")
    value = st.number_input("Temperature in Fahrenheit")
    add_btn = st.form_submit_button("Convert", type="primary")

 

    # Event handler
    def addTemp(Location, value):
        if Location and value:
            total = ((value - 32) * (5/9))
            total = round(total,2)
            print(f"My Temperature is {total}")
            return f"Your location Temperature is {total} °C"
            


if add_btn:
    display = addTemp(Location=Location, value=value)
    st.subheader(display)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "20.0°F")
col2.metric("Wind", "150 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

