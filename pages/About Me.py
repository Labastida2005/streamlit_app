import streamlit as st
from PIL import Image


image = Image.open("assets/profile.jpeg")

# ---------------- HEADER ----------------
st.title("My Personal Portfolio")
st.write("A simple portfolio built using Streamlit.")

st.divider()

# --# ---------------- ABOUT ME ----------------
st.header("About Me")

col1, col2 = st.columns([2, 1])  # text first, image right

with col1:
    st.subheader("Rizame M. Labastida 👋")

    st.write("""
I am a Computer Science student who enjoys learning programming
and building simple applications.

I like practicing coding and improving my skills step by step.
""")

    st.write("""
📅 Born on: September 20, 2005  
📍 Address: Alas, Mandaon, Masbate  
🎂 Age: 20
""")

    if st.button("Say Hello"):
        st.success("Thanks for visiting my portfolio! 👋")

with col2:
    st.image(image, use_container_width=True)

st.divider()

# ---------------- SKILLS ----------------
st.header("Skills")

st.write("Python")
st.progress(90)

st.write("HTML")
st.progress(80)

st.write("CSS")
st.progress(75)


st.divider()


# ---------------- FAVORITE SKILL ----------------
st.header("My Favorite Skill")

skill = st.selectbox(
    "Choose a skill:",
    ["Python", "HTML", "CSS"]
)

st.write(f"My selected skill is **{skill}**.")
