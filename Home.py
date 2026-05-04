import streamlit as st
from PIL import Image

image = Image.open("assets/profile.jpeg")


st.title("My Portfolio")
st.write("Simple interactive portfolio built using Streamlit.")

st.divider()


st.header("About Me")

col1, col2 = st.columns([2, 1])  # text first, image right

with col1:
    st.subheader("Rizame M. Labastida")
    st.write("""
Hello! I am a Computer Science student who enjoys learning programming
and building simple projects.

🎓 DEBESMSCAT  
📚 BSCS 3rd Year Student
""")

    if st.button("Say Hello"):
        st.success("Hello! Welcome to my portfolio 👋")

with col2:
    st.image(image, use_container_width=True)

st.divider()



st.header("🛠 Skills")

skill = st.selectbox("Choose a skill to view level:", ["C#", "Python", "C++"])

if skill == "C#":
    st.progress(60)
    st.write("Basic knowledge in C# programming.")

elif skill == "Python":
    st.progress(70)
    st.write("Good understanding of Python for projects.")

elif skill == "C++":
    st.progress(65)
    st.write("Familiar with C++ fundamentals.")

st.divider()


st.header("Projects")

project = st.radio(
    "Select a project:",
    ["Calculator App", "Portfolio Website"]
)

if project == "Calculator App":
    st.info("A simple mini calculator for basic math operations.")

elif project == "Portfolio Website":
    st.info("A personal website showcasing skills and projects.")

st.divider()



st.header("Feedback")

if st.button("Like this Portfolio"):
    st.success("Thank you for your support! ❤️")

st.caption("© 2026 Rizame M. Labastida | Built with Streamlit")
