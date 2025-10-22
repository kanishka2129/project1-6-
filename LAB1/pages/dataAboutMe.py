import streamlit as st
import random
import info

st.title("Which Disney Charecter are you?🧞")
st.write("Welcome to this quiz! Discover which Disney charecter best represents you and your personality!")
count = 0

q1 = st.radio("**QUESTION 1:** What is your favourite time of a day:",["Morning 🌅","Afternoon 🌇","Evening 🌄","Night 🌃" ])
st.write("---")
q2 = st.selectbox("**QUESTION 2:** What is your favourite vacation destination",["Disney Castle 🏰","Enchanted Forest 🌲","The Beach 🏖️","Cave of Wonders 🏜️"])
st.write("---")
q3 = st.multiselect("**QUESTION 3:** Who are your favourite fictional charecters",["Olaf ☃️","Mulan 👩🏻","Genie 🧞","Dory 🐟"])
st.write("---")
q4 = st.slider("**QUESTION 4:** How much do you belive in magic?🪄", 0,10,5)
st.write("---")
q5 = st.number_input("**QUESTION 5:** How many countries would you like to visit in your lifetime? ✈️")
st.write("---")

if st.button("Submit"):
    result = random.choice(list(info.characters.keys()))
    img = info.characters[result]
    st.metric("You are...", result)
    st.image(img)
    st.balloons()
    
