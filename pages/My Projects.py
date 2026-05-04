import streamlit as st



# ---------------- HEADER ----------------
st.title("My Project Showcase")
st.write("Simple projects I built as a Computer Science student.")

st.divider()

# ---------------- PROJECTS ----------------
st.header("Projects")

projects = [
    ("🧮 Calculator App", "A simple tool for basic arithmetic operations."),
    ("🌐 Personal Portfolio", "A website that showcases my skills and information.")
]

for title, desc in projects:
    with st.expander(title):
        st.write(desc)

st.divider()

# ---------------- OVERVIEW ----------------
st.header("Overview")

st.write("""
✔ Total Projects: 2  
✔ Main Language: Python  
✔ Framework: Streamlit  
""")

st.divider()

# ---------------- FEEDBACK ----------------
st.header("Feedback")

if st.button("👍 Like My Work"):
    st.success("Thank you for supporting my work! ❤️")

st.caption("© 2026 Project Showcase | Built with Streamlit")
