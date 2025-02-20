# steamlit

import streamlit as st
st.set_page_config(page_title="growth mindset project", project_icon="💻")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🎉 welcome to your growth journey!")
st.write("Embarace Challanges, learn from mistakes, and unlock you full potential.this AI-powered app help you to build")

# quote section
st.header("💫 Today's Growth Mindset Quote")
st.write("Success is not final; failure is not fatal: it is the courage to continue that counts. - Winston Churchill")

st.header("⚙️ what's Your Challange Today?")
user_input = st.text_input("Discribe a challange you're facing:")


# condition
if user_input:
    st.success(
        f"you re facing:{user_input}.keep pushing forward towords your goal!")
else:
    st.warning("Tell us about your challange to get started!")


# reflexing

    st.header("reflection on your Learning")
    reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(
        f"Great Insight! your reflection: {reflection}")
else:
    st.info("reflection on past experience help you grow! your defficulties")
    
    #acheivements
    st.header("celebrate your Wins!")
    acheivment = st.text_input("Share something you've recently acccomplished:")
    
    if acheivment:
        st.success(f"Amazing! you achived: {acheivment}")
    else:
        st.info("Big or small , every acheivement counts Share on now")

#footer
st.write("--------")
st.write("Keep believing in yourself. Growth is a journey, not a estination")
st.write("**Created by Ahmed zai**")

