import streamlit as st

import numpy as np

st.title("Title -> Aditya Somani")  #Title
st.header("Header -> Aditya Somani")    #Header
st.subheader("SubHeader -> Aditya Somani")  #Sub-Header
st.text("Text -> Aditya Somani")    #Text

st.markdown("# Hello")  #Markdown
st.markdown("## Hello")
st.markdown("### Hello")
st.markdown("#### Hello")
st.markdown("##### Hello")
st.markdown("###### Hello")

st.success("Data is Submitted!") #Green
st.info("Info de bhai") #Blue
st.warning("Warning") #Yellow
st.error("Error!!") #Red

st.exception(ZeroDivisionError("Division not possible by ZERO!!!")) #For exceptions

st.help(ZeroDivisionError)

st.write("range(10,12)")
st.write(range(10,12))
st.write("1+2+3")
st.write(1+2+3)
st.write({i for i in range(1,10)})

#code
st.code("x=10 \n"
        "for i in range(1,11):\n"
        "    print(i)")

#checkboxes
st.checkbox("Mail") #These True and False are "Keys" , So they cannot be same
if(st.checkbox("Box")):
        st.write("You chose Box!")

#radio button
rad=st.radio("Is the above code correct :",("True","False"))
if(rad=="True"):
        st.write("You are Correct")
else:
        st.write("Your answer is  incorrect")

#select Box
st.subheader("SelectBox")
sel=st.selectbox("Data Science :",["NONE","data analysis","web scrapping","machine learning","deep learning","NLP","Computer Vision","Image Processing"])
st.write("You've selected : "+sel)

st.subheader("Multiselect")
msb=st.multiselect("Data Science :",["NONE","data analysis","web scrapping","machine learning","deep learning","NLP","Computer Vision","Image Processing"])
st.write("You've selected : ",len(msb))
st.write("Courses are : ",msb)

#button
st.subheader("Button")
a=st.button("Dekh Kya raha he , DABA DE!!!!")
if(a):
        st.write("Daba DIYE!!!!!")

#Slider
st.subheader("Slider")
a=st.slider("Select the level ",0,100,step=1)
st.write("You've selected ",a,"%")

st.subheader("Username/Password Input")
a=st.text_input("Enter Username : ")
b=st.text_input("Enter Password : ",type="password")

st.subheader("Text Area")
ta = st.text_area("Write Something about Yourself! ")

st.subheader("NUmber Input")
y=st.number_input("Enter your age ",1,110,step=1)
if y>55:
        st.write("WOW! , You're above 55 ")

st.subheader("Date Input")
st.date_input("Enter your DOB")

st.subheader("Input time")
st.time_input("Time")